from pydantic import BaseModel


class SnippetCreate(BaseModel):
    title: str
    code: str


class SnippetOut(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True
