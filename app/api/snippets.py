from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import SessionLocal
from app.db.models import Snippet, SnippetVersion
from app.schemas.snippet import SnippetCreate, SnippetOut

router = APIRouter(prefix="/snippets")


async def get_db():
    async with SessionLocal() as s:
        yield s


@router.post("", response_model=SnippetOut)
async def create_snippet(data: SnippetCreate, db: AsyncSession = Depends(get_db)):
    snippet = Snippet(title=data.title)
    db.add(snippet)
    await db.flush()

    version = SnippetVersion(snippet_id=snippet.id, code=data.code, version=1)
    db.add(version)
    await db.commit()
    return snippet


@router.get("/{snippet_id}")
async def get_snippet(snippet_id: int, db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(Snippet).where(Snippet.id == snippet_id))
    snippet = q.scalar_one_or_none()
    if snippet is None:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet
