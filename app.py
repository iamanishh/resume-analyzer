from pip._internal.models import candidate

from services.llm_service import LLMService
from prompts.recruiter import RECRUITER_PROMPT


with open("data/sample_resume.txt", "r") as file:
    resume = file.read()

prompt = RECRUITER_PROMPT.format(
    resume = resume
)

llm = LLMService()

candidate = llm.ask(prompt)


if candidate:
    print(candidate["candidate_name"])
    print(candidate["skills"])

else:
    print("Resume analysis failed... ")

