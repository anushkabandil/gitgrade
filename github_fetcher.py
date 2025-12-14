import requests

def parse_github_url(repo_url):
    parts = repo_url.strip("/").split("/")
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo

def fetch_repo_data(repo_url):
    owner, repo = parse_github_url(repo_url)

    base_url = f"https://api.github.com/repos/{owner}/{repo}"

    repo_response = requests.get(base_url)
    commits_response = requests.get(base_url + "/commits")
    contents_response = requests.get(base_url + "/contents")
    languages_response = requests.get(base_url + "/languages")

    if repo_response.status_code != 200:
        raise Exception("Repository not found or API limit exceeded")

    repo_data = repo_response.json()

    data = {
        "repo_name": repo_data.get("name"),
        "description": repo_data.get("description"),
        "stars": repo_data.get("stargazers_count", 0),
        "forks": repo_data.get("forks_count", 0),
        "languages": list(languages_response.json().keys()) if languages_response.status_code == 200 else [],
        "commit_count": len(commits_response.json()) if commits_response.status_code == 200 else 0,
        "files": contents_response.json() if contents_response.status_code == 200 else []
    }

    return data
