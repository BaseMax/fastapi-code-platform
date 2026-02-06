import redis.asyncio as redis
from fastapi import APIRouter
from app.core.config import settings
from app.schemas.execution import ExecutionRequest

router = APIRouter(prefix="/execute")
r = redis.from_url(settings.REDIS_URL)


@router.post("")
async def enqueue_exec(req: ExecutionRequest):
    await r.lpush("exec_queue", req.model_dump_json())
    return {"status": "queued"}
