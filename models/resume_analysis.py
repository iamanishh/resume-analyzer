from pydantic import BaseModel

class ResumeAnalysis(BaseModel):
    candidate_name: str
    experience_years: str
    skills: list[str]
    overall_score: int
    strengths: list[str]
    weaknesses: list[str]
