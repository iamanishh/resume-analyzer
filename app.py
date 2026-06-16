import shutil

from fastapi import FastAPI, UploadFile, File
from pip._internal.models import candidate
from pip._internal.utils import retry

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

@app.post("/analyze", response_model=ResumeAnalysis)
def analyze_resume(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    candidate = resume_service.analyze_resume(file_path)

    return candidate
