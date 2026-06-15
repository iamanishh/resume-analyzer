import json

def parse_llm_response(response: str):
    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return None


