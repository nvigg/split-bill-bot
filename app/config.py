from dataclasses import dataclass, field

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    title: str = Field(alias="APP_TITLE", default="app")
    debug: bool = Field(alias="APP_DEBUG", default=False)
    host: str = Field(alias="APP_HOST", default="localhost")
    port: int = Field(alias="APP_PORT", default=8080)


class PostgresConfig(BaseSettings):
    host: str = Field(alias="POSTGRES_HOST", default="localhost")
    port: int = Field(alias="POSTGRES_PORT", default=5432)
    user: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    db: str = Field(alias="POSTGRES_DB")

    @property
    def url(self):
        return (
            f"postgresql+asyncpg://{self.user}:"
            f"{self.password}@{self.host}:{self.port}/{self.db}"
        )


@dataclass
class Config:
    app: AppConfig = field(default_factory=AppConfig)
    postgres: PostgresConfig = field(default_factory=PostgresConfig)


config = Config()
