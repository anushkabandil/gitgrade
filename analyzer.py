def analyze_repository(data):
    files = data.get("files", [])
    commit_count = data.get("commit_count", 0)
    languages = data.get("languages", [])

    file_names = []
    if isinstance(files, list):
        for item in files:
            name = item.get("name", "").lower()
            file_names.append(name)

    # Signals
    has_readme = any("readme" in name for name in file_names)
    has_tests = any("test" in name for name in file_names)
    structured_folders = any(
        name in ["src", "app", "lib"] for name in file_names
    )

    signals = {
        "has_readme": has_readme,
        "has_tests": has_tests,
        "structured_folders": structured_folders,
        "commit_count": commit_count,
        "file_count": len(file_names),
        "language_count": len(languages)
    }

    return signals

def extract_skills(data):
    skills = []

    # Languages directly represent technical skills
    for lang in data.get("languages", []):
        skills.append(lang)

    # Git usage as a skill
    if data.get("commit_count", 0) >= 3:
        skills.append("Version Control (Git)")

    # Documentation skill
    if data.get("description"):
        skills.append("Technical Documentation")

    return list(set(skills))
