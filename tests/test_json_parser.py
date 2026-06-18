from utils.json_parser import parse_llm_response

def test_parse_valid_json():

    response = """
     {
       "candidate_name": "John",
       "experience_years": "3"
     }
     """

    result = parse_llm_response(response)

    assert result["candidate_name"] == "John"
    assert result["experience_years"] == "3"