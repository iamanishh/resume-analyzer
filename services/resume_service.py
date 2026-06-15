from prompts.recruiter import RECRUITER_PROMPT
from services.llm_service import LLMService

class ResumeService:
    def __init__(self):
        self.llm = LLMService()

    def analyze_resume(self, resume_path: str):
        with open(resume_path, "r") as file:
            resume = file.read()

        prompt = RECRUITER_PROMPT.format(
            resume=resume
        )
        return self.llm.analyze_resume(prompt)