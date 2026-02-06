from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.models import Base
from app.db.session import engine
from app.api import snippets, execute

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title="Code Snippet Execution Platform", lifespan=lifespan)

app.include_router(snippets.router)
app.include_router(execute.router)
