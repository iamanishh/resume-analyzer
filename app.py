from services.resume_service import ResumeService

def main():
    resume_service = ResumeService()

    candidate = resume_service.analyze_resume(
        "data/sample_resume.txt"
    )

    if candidate:
        print("\nResume Analysis")
        print("-" * 30)

        print(f"Candidate : {candidate['candidate_name']}")
        print(f"Experience : {candidate['experience_years']} years")
        print(f"Score : {candidate['overall_score']}")

        print("\nSkills")
        for skill in candidate['skills']:
            print(f"- {skill}")

        print("\nStrengths")
        for strength in candidate['strengths']:
            print(f"- {strength}")

        print("\nWeaknesses")
        for weakness in candidate['weaknesses']:
            print(f"- {weakness}")

    else:
        print("Resume analysis failed... ")


if __name__ == "__main__":
    main()



