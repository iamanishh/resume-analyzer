from ollama import chat
from utils.json_parser import parse_llm_response


class LLMService:

    def ask(self, prompt: str):
        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return parse_llm_response(
            response["messages"]["content"]
        )