from prompts.recruiter import RECRUITER_PROMPT
from services.llm_service import LLMService
from services.document_service import DocumentService

class ResumeService:

    def __init__(self):
        self.document_service = DocumentService()
        self.llm = LLMService()

    def analyze_resume(self, resume_path: str):
        resume = self.document_service.extract_text(
            resume_path
        )

        prompt = RECRUITER_PROMPT.format(
            resume=resume
        )
        return self.llm.analyze_resume(prompt)