from models.models import *
import dspy


class ProblemGenerationSignature(dspy.Signature):
    """Given a job description, list all of the perceived and real problems and obstacles that the job poster could or is currently facing."""

    job_description: str = dspy.InputField()
    problems: list[Problem] = dspy.OutputField()


class ObjectionGenerationSignature(dspy.Signature):
    """Given a problem and sub ploblems, generate a list of all possible objections that the customer may have for why they think they couldn't solve that problem."""

    problem: str = dspy.InputField()
    objections: list[Objection] = dspy.OutputField()


class SubProblemGenerationSignature(dspy.Signature):
    """Given a problem/obstacle
    Break down the given problem/obstacle into very intricate steps that the job poster would have to do/take in order to be successful.
    """

    problem: str = dspy.InputField()
    sub_problems: list[SubProblem] = dspy.OutputField()


class ProblemSolvingSignature(dspy.Signature):
    """Given an objection and a problem, generate single sentences on how a single person service provider would deliver a one-on-one solution. Generate solutions for the following delivery methods: done with you, done for you, and done by you solutions for the given objections. Generate 5 solutions for each method.
    Example:
    Problem: Buying healthy food, and grocery shopping is hard, confusing, i won't like it. I will suck at it.

    Solution 1: In-person grocery shopping, where I take clients to the store and teach them how to shop
    Solution 2: Personalized grocery list, where I teach them how to make their list
    Solution 3: Full-service shopping, where I buy their food for them. 100 percent done for them.
    Solution 4: In-Person orientation (not at store), where I teach them what to get
    Solution 5: Text support while shopping, where I help them if they get stuck
    Solution 6: Phone call while grocery shopping, where I plan to call when they go shopping to provide direction and support
    """

    problem: str = dspy.InputField()
    objections: str = dspy.InputField()
    solutions: Solution = dspy.OutputField()