from fastapi import FastAPI
from services.resume_service import ResumeService
from models.resume_analysis import ResumeAnalysis
app = FastAPI()

resume_service = ResumeService()


@app.get("/")
def home():
    return {
        "message" : "Resume analyzer API is running"
    }

@app.get("/analyze", response_model=ResumeAnalysis)
def analyze_resume():
    candidate = resume_service.analyze_resume(
        "data/sample_resume.pdf"
    )

    if candidate:
        return candidate

    return {
        "error": "Resume alaysis failed... "
    }
