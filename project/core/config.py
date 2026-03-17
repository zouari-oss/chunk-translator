"""
Module: config.py

Project configuration handler

Author: @ZouariOmar (zouariomar20@gmail.com)
Date: 2026-03-17
License: GPL3.0
Version: 0.1
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    API_V1_STR: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings from environment or .env file."""
    return Settings()  # pyright: ignore


settings = get_settings()
