from ollama import chat
from config.settings import MODEL_NAME
from utils.json_parser import parse_llm_response


class LLMService:

    def analyze_resume(self, prompt: str):

        for attempt in range(2):

            response = chat(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            candidate = parse_llm_response(
                response["message"]["content"]
            )

            if candidate:
                print(f"LLM succeeded on attempt {attempt + 1}")
                return candidate

            print(f"Retrying... attempt {attempt + 1}")

        return None