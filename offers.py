import os
from dsp.modules import anthropic
from dotenv import load_dotenv
from data.example_1 import customer_problem
from modules.modules import *
from fastapi import FastAPI
load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
# claude-3-5-sonnet-20240620
# claude-3-haiku-20240307
client = anthropic.Claude(
    model="claude-3-5-sonnet-20240620", max_tokens=4000, api_key=anthropic_api_key
)
dspy.settings.configure(lm=client)



app = FastAPI()

@app.post("/generate", response_model=OfferGenerationPack)
async def generate_offers(job_description: OfferInput) -> OfferGenerationPack:
    if job_description.job_description == "":
        return ValueError
    offer_gen = OfferGenerationModule(client)
    offer_gen_solutions = offer_gen(job_description=job_description.job_description)
    problems = offer_gen_solutions.problem
    subs = offer_gen_solutions.sub_problems
    objections = offer_gen_solutions.objections
    solutions = offer_gen_solutions.solutions
    return offer_gen_solutions

