from prompts.recruiter import RECRUITER_PROMPT
from services.llm_service import LLMService
from services.document_service import DocumentService
from utils.logger import logger
from prompts.job_match import JOB_MATCH_PROMPT

class ResumeService:

    def __init__(self):
        self.document_service = DocumentService()
        self.llm = LLMService()

    def analyze_resume(self, pdf_path, job_description):

        logger.info(f"Starting resume analysis...")

        resume = self.document_service.extract_text(
            pdf_path
        )

        logger.info(f"Preparing recruiter prompt")

        if job_description:
            prompt = JOB_MATCH_PROMPT.format(
                resume=resume,
                job_description=job_description,
            )
        else:
            prompt = RECRUITER_PROMPT.format(
                resume=resume
                )

        logger.info(f"Sending prompt to LLM")

        return self.llm.analyze_resume(prompt)

