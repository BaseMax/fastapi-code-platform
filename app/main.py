from fastapi import FastAPI
from app.api import snippets, execute

app = FastAPI(title="Code Snippet Execution Platform")

app.include_router(snippets.router)
app.include_router(execute.router)
