import logging
import os

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME", "fastapi-postgresql-crud")
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


def get_settings() -> BaseSettings:
    log.info("Loading env settings")
    return Settings()
