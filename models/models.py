from pydantic import BaseModel, Field

class OfferInput(BaseModel):
    job_description: str

class Problem(BaseModel):
    """Real or percieved problem that the job poster could experience, related to the job description."""

    problem: str


class SubProblem(BaseModel):
    """Break down given problem/obstacle into very intricate step that the job poster would have to do/take in order to be successful"""

    sub_problems: str


class Objection(BaseModel):
    """Objection that the customer may have for why they think they couldn't solve the problem/subproblem"""

    objection: str


class Solution(BaseModel):
    """single sentences on how a single person service provider would deliver a one-on-one solution. Solutions for the following delivery methods: done with you, done for you, and done by you solutions for the given objections."""

    done_with_you_solutions: list[str] = Field(
        ..., description="One on One solutions that are done with the client."
    )
    done_for_you_solutions: list[str] = Field(
        ..., description="One on One solutions that are done for the client."
    )
    do_it_yourself_solutions: list[str] = Field(
        ..., description="One on One solutions that are done by the client."
    )


class OfferGenerationPack(BaseModel):
    problem: list[Problem]
    sub_problems: list[list[SubProblem]]
    objections: list[list[Objection]]
    solutions: list[Solution]
