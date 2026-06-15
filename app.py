from ollama import chat
from prompts import RECRUITER_PROMPT
from utils import parse_llm_response

with open("sample_resume.txt", "r") as file:
    resume = file.read()

prompt = RECRUITER_PROMPT.format(
    resume = resume
)

response = chat(
    model="llama3.2:3b",
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
    print(candidate["candidate_name"])
    print(candidate["skills"])

else:
    print("Resume analysis failed... ")

