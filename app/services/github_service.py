import requests
from app.config import GITHUB_TOKEN, GITHUB_API_URL

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user_repos(username: str):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {
            "error": "Failed to fetch repositories",
            "details": response.json()
        }

    return response.json()


def create_issue(owner: str, repo: str, title: str, body: str = None):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code not in [200, 201]:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json().get("message", "GitHub API error")
            }

        return response.json()

    except Exception as e:
        return {
            "error": True,
            "message": str(e)
        }
        

def list_issues(owner: str, repo: str, state: str = "open"):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"

    params = {
        "state": state
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json().get("message", "GitHub API error")
            }

        issues = response.json()

        # Clean response (only useful fields)
        cleaned_issues = [
            {
                "id": issue.get("id"),
                "title": issue.get("title"),
                "state": issue.get("state"),
                "url": issue.get("html_url"),
                "created_at": issue.get("created_at")
            }
            for issue in issues
        ]

        return cleaned_issues

    except Exception as e:
        return {
            "error": True,
            "message": str(e)
        }