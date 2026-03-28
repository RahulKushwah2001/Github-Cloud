from fastapi import APIRouter, HTTPException, Query
from app.services.github_service import get_user_repos, create_issue, list_issues
from app.models.issue import IssueCreate

router = APIRouter()

@router.get("/repos/{username}")
def fetch_repos(username: str):
    return get_user_repos(username)


@router.post("/create-issue")
def create_issue_api(issue: IssueCreate):
    response = create_issue(
        owner=issue.owner,
        repo=issue.repo,
        title=issue.title,
        body=issue.body
    )

    if "error" in response:
        raise HTTPException(status_code=400, detail=response)

    return {
        "message": "Issue created successfully",
        "data": response
    }
    
    
@router.get("/list-issues")
def list_issues_api(
    owner: str,
    repo: str,
    state: str = Query("open", enum=["open", "closed", "all"])
):
    response = list_issues(owner, repo, state)

    if isinstance(response, dict) and response.get("error"):
        raise HTTPException(
            status_code=response.get("status_code", 500),
            detail=response.get("message")
        )

    return {
        "count": len(response),
        "issues": response
    }