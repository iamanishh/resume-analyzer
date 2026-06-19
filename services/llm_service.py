from ollama import Client
from config.settings import MODEL_NAME, OLLAMA_BASE_URL
from utils.json_parser import parse_llm_response
from utils.logger import logger

class LLMService:
    def analyze_resume(self, prompt: str):

        client = Client(host=OLLAMA_BASE_URL)

        candidate = None

        for attempt in range(2):

            response = client.chat(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                options={
                    "temperature": 0,
                    "top_p": 0.9,
                    "num_predict": 1024
                }
            )

            candidate = parse_llm_response(
                response["message"]["content"]
            )

            required_fields = [
                "candidate_name",
                "overall_score",
                "matching_skills",
                "missing_skills",
                "strengths",
                "weaknesses",
                "recommendation"
            ]

            is_valid = (
                    candidate is not None
                    and all(field in candidate for field in required_fields)
                    and candidate["recommendation"] != ""
                    and len(candidate["strengths"]) > 0
                    and len(candidate["weaknesses"]) > 0
            )

            if is_valid:
                logger.info(
                    f"LLM succeeded on attempt {attempt + 1}"
                )
                return candidate

            logger.warning(
                f"Incomplete LLM response. Retrying..."
            )

        # ---------- Loop finished ----------

        logger.warning(
            "LLM returned incomplete response. Filling defaults."
        )

        if candidate:

            if not candidate.get("strengths"):
                candidate["strengths"] = [
                    "Technical experience found in the resume."
                ]

            if not candidate.get("weaknesses"):
                candidate["weaknesses"] = [
                    "No specific weaknesses identified."
                ]

            if not candidate.get("recommendation"):
                candidate["recommendation"] = (
                    "Further manual review is recommended."
                )

            return candidate

        logger.error("LLM failed after all retry attempts")

        return None