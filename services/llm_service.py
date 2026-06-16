from ollama import chat
from utils.json_parser import parse_llm_response
from config.settings import MODEL_NAME

class LLMService:

    def analyze_resume(self, prompt: str):
        response = chat(
            model= MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return parse_llm_response(
            response["message"]["content"]
        )