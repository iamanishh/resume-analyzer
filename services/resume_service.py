from prompts.recruiter import RECRUITER_PROMPT
from services.llm_service import LLMService
from services.document_service import DocumentService
from utils.logger import logger

class ResumeService:

    def __init__(self):
        self.document_service = DocumentService()
        self.llm = LLMService()

    def analyze_resume(self, resume_path: str):

        logger.info(f"Starting resume analysis...")

        resume = self.document_service.extract_text(
            resume_path
        )

        logger.info(f"Preparing recruiter prompt")

        prompt = RECRUITER_PROMPT.format(
            resume=resume
        )

        logger.info(f"Sending prompt to LLM")

        return self.llm.analyze_resume(prompt)