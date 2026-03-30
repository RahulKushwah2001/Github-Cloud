from pydantic import BaseModel

class IssueCreate(BaseModel):
    owner: str
    repo: str
    title: str
    body: str | None = None
    
class PullRequestCreate(BaseModel):
    owner: str
    repo: str
    title: str
    head: str   # source branch
    base: str   # target branch
    body: str | None = None