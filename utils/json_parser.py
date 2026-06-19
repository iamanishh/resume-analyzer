import json
from utils.logger import logger

def parse_llm_response(response: str):
    try:
        response = response.strip()
        if response.count("{") > response.count("}"):
            response += "}"

        return json.loads(response)

    except Exception as e:
        logger.error("JSON to parse LLM response...")

        logger.error(e)

        logger.error(response)

        return None


