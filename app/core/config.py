from pydantic import BaseModel


class Settings(BaseModel):
    DB_URL: str = "mysql+aiomysql://app:app@mariadb:3306/code"
    REDIS_URL: str = "redis://redis:6379/0"
    SANDBOX_CONTAINER: str = "code-sandbox"
    EXEC_TIMEOUT: int = 5
    MAX_OUTPUT: int = 20000


settings = Settings()
