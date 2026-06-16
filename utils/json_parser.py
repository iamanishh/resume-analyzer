import json

def parse_llm_response(response: str):
    try:
        return json.loads(response)

    except Exception as e:
        print("JSON parsing error ...")

        print(e)

        print(response)

        return None


