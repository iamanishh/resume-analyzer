RECRUITER_PROMPT = """ 
 You are a senior technical recruiter.

 Analyze the following resume.

 Return only valid JSON.

 The JSON must contain:
 {{
  "candidate_name": "",
  "experience_years": ",
  "skills": [],
  "overall_score": 0,
  "strengths": [],
  "weaknesses": []
  }}

  Resume: 

  {resume}
 """