from github_fetcher import fetch_repo_data
from analyzer import analyze_repository
from scorer import score_repository
from roadmap import generate_roadmap
from summary import generate_summaries, generate_score_explanation
from analyzer import extract_skills
from roadmap import explain_roadmap




def main():
    print("GitGrade - GitHub Repository Evaluator")
    repo_url = input("Enter GitHub Repository URL: ")

    try:
        data = fetch_repo_data(repo_url)
        signals = analyze_repository(data)
        skills = extract_skills(data)

        scores, overall_score, level, recruiter_confidence = score_repository(signals)


        recruiter_summary, student_summary = generate_summaries(scores, level)
        roadmap = generate_roadmap(scores)

        print("\n================ Repository Evaluation ================\n")

        print("Dimension-wise Scores:")
        for key, value in scores.items():
            print(f"- {key}: {value}/10")

        print(f"\nOverall Score: {overall_score}/10")
        print(f"Repository Level: {level}")
        print(f"Recruiter Confidence Level: {recruiter_confidence}")
        print("\nDetected Skills (Resume-Ready):")
        for skill in skills:
            print("-", skill)


        print("\nRecruiter Perspective:")
        print(recruiter_summary)

        print("\nStudent Perspective:")
        print(student_summary)

        print("\nPersonalized Roadmap:")
        for idx, step in enumerate(roadmap, start=1):
            print(f"{idx}. {step}")

        print("\nWhy This Roadmap?")
        print(explain_roadmap(roadmap))


        print("\nWhy These Scores?")
        score_explanation = generate_score_explanation(scores)

        for point in score_explanation:
            print("-", point)


        

        print("\n=======================================================\n")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
