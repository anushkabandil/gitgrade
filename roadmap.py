def generate_roadmap(scores):
    roadmap = []

    if scores.get("Documentation", 0) < 6:
        roadmap.append("Add a detailed README with project overview, setup steps, and usage instructions.")

    if scores.get("Testing", 0) < 6:
        roadmap.append("Introduce unit tests for core functionality to improve reliability and maintainability.")

    if scores.get("Project Structure", 0) < 6:
        roadmap.append("Refactor the project into a cleaner folder structure (e.g., src/, tests/, docs/).")

    if scores.get("Git Practices", 0) < 6:
        roadmap.append("Improve commit consistency and use meaningful commit messages.")

    if scores.get("Code Quality", 0) < 6:
        roadmap.append("Refactor large files into smaller modules and improve code readability.")

    # Advanced suggestions (always optional)
    roadmap.append("Set up basic CI/CD using GitHub Actions.")
    roadmap.append("Add issue templates and contribution guidelines.")

    return roadmap
