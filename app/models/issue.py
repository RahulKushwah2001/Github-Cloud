from pydantic import BaseModel

class IssueCreate(BaseModel):
    owner: str
    repo: str
    title: str
    body: str | None = None