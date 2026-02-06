import docker
from app.core.config import settings

client = docker.from_env()


def run_code(code: str) -> str:
    container = client.containers.get(settings.SANDBOX_CONTAINER)

    exec_id = client.api.exec_create(
        container.id,
        cmd=["python", "/runner.py"],
        stdin=True,
        tty=False,
    )

    output = client.api.exec_start(exec_id, stdin=True, socket=False, demux=False, stream=False, detach=False, tty=False, input=code.encode())
    return output.decode(errors="ignore")[: settings.MAX_OUTPUT]
