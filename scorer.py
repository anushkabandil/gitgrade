def score_repository(signals):
    scores = {}

    # Documentation
    if signals["has_readme"]:
        scores["Documentation"] = 7
    else:
        scores["Documentation"] = 4

    # Testing
    if signals["has_tests"]:
        scores["Testing"] = 7
    else:
        scores["Testing"] = 4

    # Project Structure
    if signals["structured_folders"]:
        scores["Project Structure"] = 7
    else:
        scores["Project Structure"] = 4

    # Git Practices
    if signals["commit_count"] >= 10:
        scores["Git Practices"] = 8
    elif signals["commit_count"] >= 5:
        scores["Git Practices"] = 6
    elif signals["commit_count"] >= 2:
        scores["Git Practices"] = 5
    else:
        scores["Git Practices"] = 3

    # Code Quality
    if signals["file_count"] >= 10:
        scores["Code Quality"] = 7
    else:
        scores["Code Quality"] = 5

    # Overall Score
    overall_score = round(sum(scores.values()) / len(scores), 1)

    # Repository Level
    if overall_score < 4:
        level = "Beginner"
    elif overall_score < 7:
        level = "Intermediate"
    else:
        level = "Industry-Ready"

    # Recruiter Confidence Level
    if overall_score >= 7:
        recruiter_confidence = "High"
    elif overall_score >= 5:
        recruiter_confidence = "Medium"
    else:
        recruiter_confidence = "Low"

    return scores, overall_score, level, recruiter_confidence

