def generate_summaries(scores, level):
    strengths = []
    weaknesses = []

    for dimension, score in scores.items():
        if score >= 7:
            strengths.append(dimension)
        elif score <= 4:
            weaknesses.append(dimension)

    # Recruiter Summary
    recruiter_summary = "The repository "

    if strengths:
        recruiter_summary += "shows strong " + ", ".join(strengths)
    else:
        recruiter_summary += "has limited strengths"

    if weaknesses:
        recruiter_summary += " but lacks sufficient " + ", ".join(weaknesses) + "."
    else:
        recruiter_summary += " with no major weaknesses."

    # Student Summary
    student_summary = f"This project is currently at an {level} level. "

    if weaknesses:
        student_summary += (
            "To improve, focus on strengthening "
            + ", ".join(weaknesses)
            + " to make the repository more industry-ready."
        )
    else:
        student_summary += "Great job! Continue refining and scaling this project."

    return recruiter_summary, student_summary
