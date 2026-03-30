import requests
from app.config import GITHUB_TOKEN, GITHUB_API_URL


HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


#Fetch RepO
def get_user_repos(username: str):
    url = f"{GITHUB_API_URL}/users/{username}/repos"

    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json().get("message", "Failed to fetch repositories")
            }

        repos_data = response.json()

        # return only useful fields
        repos_list = []
        for repo in repos_data:
            repos_list.append({
                "id": repo.get("id"),
                "name": repo.get("name"),
                "url": repo.get("html_url"),
                "private": repo.get("private")
            })

        return repos_list

    except requests.exceptions.RequestException as e:
        return {
            "error": True,
            "message": str(e)
        }


#Create Issue
def create_issue(owner: str, repo: str, title: str, body: str = None):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    try:
        response = requests.post(url, headers=HEADERS, json=payload)

        if response.status_code not in [200, 201]:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json().get("message", "Failed to create issue")
            }

        issue_data = response.json()

        return {
            "id": issue_data.get("id"),
            "title": issue_data.get("title"),
            "url": issue_data.get("html_url"),
            "state": issue_data.get("state")
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": True,
            "message": str(e)
        }


# List Issues
def list_issues(owner: str, repo: str, state: str = "open"):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"
    params = {"state": state}

    try:
        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code != 200:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json().get("message", "Failed to fetch issues")
            }

        issues_data = response.json()

        issues_list = []
        for issue in issues_data:
            issues_list.append({
                "id": issue.get("id"),
                "title": issue.get("title"),
                "state": issue.get("state"),
                "url": issue.get("html_url"),
                "created_at": issue.get("created_at")
            })

        return issues_list

    except requests.exceptions.RequestException as e:
        return {
            "error": True,
            "message": str(e)
        }


# Fetch Commits
def get_commits(owner: str, repo: str):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json().get("message", "Failed to fetch commits")
            }

        commits_data = response.json()

        commits_list = []
        for commit in commits_data:
            commits_list.append({
                "sha": commit.get("sha"),
                "message": commit.get("commit", {}).get("message"),
                "author": commit.get("commit", {}).get("author", {}).get("name"),
                "date": commit.get("commit", {}).get("author", {}).get("date"),
                "url": commit.get("html_url")
            })

        return commits_list

    except requests.exceptions.RequestException as e:
        return {
            "error": True,
            "message": str(e)
        }


# Create PR
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = None):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls"

    payload = {
        "title": title,
        "head": head,
        "base": base,
        "body": body
    }

    try:
        response = requests.post(url, headers=HEADERS, json=payload)

        if response.status_code not in [200, 201]:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json().get("message", "Failed to create pull request")
            }

        pr_data = response.json()

        return {
            "id": pr_data.get("id"),
            "title": pr_data.get("title"),
            "url": pr_data.get("html_url"),
            "state": pr_data.get("state")
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": True,
            "message": str(e)
        }