from signatures.offer_signatures import *
from langfuse.decorators import observe, langfuse_context

class ProblemGenerationModule(dspy.Module):
    def __init__(self, client):
        super().__init__()
        self.problems = dspy.TypedPredictor(ProblemGenerationSignature)
        self.client = client

    @observe(
        as_type="generation",
        name="problem_generation",
    )
    def forward(self, job_description) -> list[Problem]:
        problems = self.problems(job_description=job_description).problems
        langfuse_context.update_current_observation(
            input=job_description,
            usage={
                "input": self.client.history[-1]["response"].usage.input_tokens,
                "output": self.client.history[-1]["response"].usage.output_tokens,
            },
            model=self.client.history[-1]["kwargs"]["model"],
        )
        return problems


class SubProblemGenerationModule(dspy.Module):
    def __init__(self, client):
        super().__init__()
        self.sub_problems = dspy.TypedPredictor(SubProblemGenerationSignature)
        self.client = client

    @observe(as_type="generation", name="sub_problem_generation")
    def forward(self, problems: list[Problem]) -> list[SubProblem]:
        sub_problems = []
        input_tokens = 0
        output_tokens = 0
        for problem in problems:
            sub_problems.append(self.sub_problems(problem=problem.problem).sub_problems)
            input_tokens += self.client.history[-1]["response"].usage.input_tokens
            output_tokens += self.client.history[-1]["response"].usage.output_tokens
        langfuse_context.update_current_observation(
            input=problems,
            usage={
                "input": input_tokens,
                "output": output_tokens,
            },
            model=self.client.history[-1]["kwargs"]["model"],
        )
        return sub_problems


class ObjectionGenerationModule(dspy.Module):
    def __init__(self, client):
        super().__init__()
        self.objections = dspy.TypedPredictor(ObjectionGenerationSignature)
        self.client = client

    def create_problem_subproblem_string(self, problem, sub_problems):
        problem_str = f"Problem:\n{problem.problem}\n"
        sub_problem_str = "Sub_problem\n" + "\nSub_problem\n".join(
            [x.sub_problems for x in sub_problems]
        )
        return problem_str + sub_problem_str

    @observe(as_type="generation", name="objection_generation")
    def forward(
        self, problems: list[Problem], sub_problems: list[SubProblem]
    ) -> list[SubProblem]:
        objections = []
        input_tokens = 0
        output_tokens = 0
        for idx, problem in enumerate(problems):
            current_str = self.create_problem_subproblem_string(
                problem, sub_problems[idx]
            )
            objections.append(self.objections(problem=current_str).objections)
            input_tokens += self.client.history[-1]["response"].usage.input_tokens
            output_tokens += self.client.history[-1]["response"].usage.output_tokens

        langfuse_context.update_current_observation(
            input={"problems": problems, "sub_problems": sub_problems},
            usage={
                "input": input_tokens,
                "output": output_tokens,
            },
            model=self.client.history[-1]["kwargs"]["model"],
        )
        return objections


class SolutionGenerationModule(dspy.Module):
    def __init__(self, client):
        super().__init__()
        self.solutions = dspy.TypedPredictor(ProblemSolvingSignature)
        self.client = client

    def create_problem_subproblem_string(self, problem, sub_problems):
        problem_str = f"Problem:\n{problem.problem}\n"
        sub_problem_str = "Sub_problem\n" + "\nSub_problem\n".join(
            [x.sub_problems for x in sub_problems]
        )

        return problem_str + sub_problem_str

    def create_objection_str(self, objections):
        return "Objection\n" + "\nObjection\n".join([x.objection for x in objections])

    @observe(as_type="generation", name="solution_generation")
    def forward(
        self,
        problems: list[Problem],
        sub_problems: list[SubProblem],
        objections: list[Objection],
    ) -> list[SubProblem]:
        solutions = []
        input_tokens = 0
        output_tokens = 0
        for idx, problem in enumerate(problems):
            current_str = self.create_problem_subproblem_string(
                problem, sub_problems[idx]
            )
            objection_str = self.create_objection_str(objections[idx])
            solutions.append(
                self.solutions(problem=current_str, objections=objection_str).solutions
            )
            input_tokens += self.client.history[-1]["response"].usage.input_tokens
            output_tokens += self.client.history[-1]["response"].usage.output_tokens
        langfuse_context.update_current_observation(
            input={
                "problems": problems,
                "sub_problems": sub_problems,
                "objections": objections,
            },
            usage={
                "input": input_tokens,
                "output": output_tokens,
            },
            model=self.client.history[-1]["kwargs"]["model"],
        )
        return solutions


class OfferGenerationModule(dspy.Module):
    def __init__(self, client):
        super().__init__()
        self.problems = ProblemGenerationModule(client=client)
        self.sub_problems = SubProblemGenerationModule(client=client)
        self.objections = ObjectionGenerationModule(client=client)
        self.solutions = SolutionGenerationModule(client=client)

    @observe(name="OfferGenerationModule")
    def forward(self, job_description):
        problems = self.problems(job_description=job_description)
        sub_problems = self.sub_problems(problems)
        objections = self.objections(problems, sub_problems)
        solutions = self.solutions(problems, sub_problems, objections)
        return OfferGenerationPack(
            problem=problems,
            sub_problems=sub_problems,
            objections=objections,
            solutions=solutions,
        )