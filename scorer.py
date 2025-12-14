def score_repository(signals):
    scores = {}

    # Documentation
    scores["Documentation"] = 8 if signals["has_readme"] else 3

    # Testing
    scores["Testing"] = 8 if signals["has_tests"] else 2

    # Project Structure
    scores["Project Structure"] = 7 if signals["structured_folders"] else 4

    # Git Practices
    if signals["commit_count"] >= 10:
        scores["Git Practices"] = 8
    elif signals["commit_count"] >= 5:
        scores["Git Practices"] = 6
    else:
        scores["Git Practices"] = 3

    # Code Quality (proxy using file & language count)
    if signals["file_count"] >= 10 and signals["language_count"] >= 1:
        scores["Code Quality"] = 7
    else:
        scores["Code Quality"] = 5

    # Overall Score
    overall_score = round(sum(scores.values()) / len(scores), 1)

    # Repo Maturity Level
    if overall_score < 4:
        level = "Beginner"
    elif overall_score < 7:
        level = "Intermediate"
    else:
        level = "Industry-Ready"

    return scores, overall_score, level
