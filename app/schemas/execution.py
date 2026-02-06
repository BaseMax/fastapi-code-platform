from pydantic import BaseModel


class ExecutionRequest(BaseModel):
    snippet_version_id: int


class ExecutionOut(BaseModel):
    id: int
    status: str
    output: str

    class Config:
        from_attributes = True
