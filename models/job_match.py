from pydantic import BaseModel

class JobMatchAnalysis(BaseModel):
    candidate_name: str
    overall_score: int
    matching_skills: list[str]
    missing_skills: list[str]
    strengths: list[str]
    weaknesses: list[str]
    recommendation: str