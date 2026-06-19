from fastapi import FastAPI,Form, UploadFile, File, HTTPException

from models.job_match import JobMatchAnalysis
from services.resume_service import ResumeService
from models.resume_analysis import ResumeAnalysis
from exceptions.handlers import register_exception_handlers
from utils.file_manager import FileManager

app = FastAPI(
    title="Resume Analyzer API",
    description="""
AI-powered Resume Analyzer built with FastAPI and Ollama.

Features:
- Resume Analysis
- Resume vs Job Matching
- PDF Upload
- LLM Powered Skill Extraction
""",
    version="1.0.0",
)


register_exception_handlers(app)

resume_service = ResumeService()

def validate_pdf(file: UploadFile):

    if not file.filename:
        raise HTTPException(
            status_code=415,
            detail="No filename provided."
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=415,
            detail="Only PDF files are allowed."
        )


@app.get("/", tags=["Health"])
def home():
    return {
        "status": "healthy",
        "service" : "Resume analyzer API"
    }

@app.post("/analyze",
          tags=["Resume Analysis"],
          summary="Analyze a resume PDF",
          description="""
Upload a PDF resume.

Returns:

- Candidate Name
- Experience
- Skills
- Strengths
- Weaknesses
""",
          response_model=ResumeAnalysis)
def analyze_resume(file: UploadFile = File(...)):

    validate_pdf(file)
    file_path = FileManager.save(file)

    try:
        candidate = resume_service.analyze_resume(file_path)

        if candidate is None:
            raise HTTPException(
                status_code=500,
                detail="Resume analysis failed..."
            )
        return candidate
    finally:
        FileManager.delete(file_path)


@app.post("/analyze/match",
          tags=["Job Matching"],
          summary="Compare resume against a job description",
          response_model=JobMatchAnalysis)
def analyze_resume_against_job(file: UploadFile = File(...),
                               job_description: str = Form(...)):

    validate_pdf(file)
    file_path = FileManager.save(file)

    try:
        candidate = resume_service.analyze_resume(file_path,job_description)
        if candidate is None:
            raise HTTPException(
                status_code=500,
                detail="Resume analysis failed..."
            )
        return candidate
    finally:
        FileManager.delete(file_path)


