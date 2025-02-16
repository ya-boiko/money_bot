"""Settings."""

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class TgSettings(BaseModel):
    """Telegram settings."""

    token: str = ""
    users: str = ""


class Settings(BaseSettings):
    """Settings."""

    model_config = SettingsConfigDict(env_nested_delimiter="__")

    tg: TgSettings = TgSettings()
