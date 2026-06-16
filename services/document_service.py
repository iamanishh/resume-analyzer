import fitz
from utils.logger import logger

class DocumentService:

    def extract_text(self, file_path: str) -> str:

        logger.info(f"Extracting text from {file_path}")

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        logger.info(f" PDF parsed successfully")

        return text
