from fastapi import APIRouter, HTTPException, Query
from app.services.github_service import (get_user_repos, create_issue, list_issues, get_commits, create_pull_request)
from app.models.github import IssueCreate, PullRequestCreate

router = APIRouter()

def handle_error(response):
    if isinstance(response, dict) and response.get("error"):
        raise HTTPException(
            status_code=response.get("status_code", 500),
            detail=response.get("message")
        )
    return response


@router.get("/repos/{username}")
def fetch_repos(username: str):
    if not username.strip():
        raise HTTPException(status_code=400, detail="Username cannot be empty")

    response = get_user_repos(username)
    return handle_error(response)


@router.post("/create-issue")
def create_issue_api(issue: IssueCreate):
    response = create_issue(
        issue.owner, issue.repo, issue.title, issue.body
    )
    return {
        "message": "Issue created successfully",
        "data": handle_error(response)
    }


@router.get("/list-issues")
def list_issues_api(
    owner: str,
    repo: str,
    state: str = Query("open", enum=["open", "closed", "all"])
):
    response = list_issues(owner, repo, state)
    return {
        "count": len(response),
        "issues": handle_error(response)
    }


@router.get("/commits")
def get_commits_api(owner: str, repo: str):
    response = get_commits(owner, repo)
    return {
        "count": len(response),
        "commits": handle_error(response)
    }


@router.post("/create-pull-request")
def create_pr_api(pr: PullRequestCreate):
    response = create_pull_request(
        pr.owner, pr.repo, pr.title, pr.head, pr.base, pr.body
    )
    return {
        "message": "Pull request created successfully",
        "data": handle_error(response)
    }