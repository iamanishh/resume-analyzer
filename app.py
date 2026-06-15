from fastapi import FastAPI
from services.resume_service import ResumeService

app = FastAPI()

resume_service = ResumeService()


@app.get("/")
def home():
    return {
        "message" : "Resume analyzer API is running"
    }

@app.get("/analyze")
def analyze_resume():
    candidate = resume_service.analyze_resume(
        "data/sample_resume.txt"
    )

    if candidate:
        return candidate

    return {
        "error": "Resume alaysis failed... "
    }
