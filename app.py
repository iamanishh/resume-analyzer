from ollama import chat
from prompts import RECRUITER_PROMPT

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
print(response["message"]["content"])

