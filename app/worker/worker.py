import asyncio
import json
import redis.asyncio as redis
from sqlalchemy import select
from app.core.config import settings
from app.db.session import SessionLocal
from app.db.models import SnippetVersion, Execution
from app.services.executor import run_code

r = redis.from_url(settings.REDIS_URL)


async def worker():
    while True:
        _, data = await r.brpop("exec_queue")
        job = json.loads(data)

        async with SessionLocal() as db:
            q = await db.execute(
                select(SnippetVersion).where(
                    SnippetVersion.id == job["snippet_version_id"]
                )
            )
            version = q.scalar_one()

            try:
                output = run_code(version.code)
                status = "done"
            except Exception as e:
                output = str(e)
                status = "error"

            db.add(
                Execution(
                    snippet_version_id=version.id,
                    output=output,
                    status=status,
                )
            )
            await db.commit()


asyncio.run(worker())
