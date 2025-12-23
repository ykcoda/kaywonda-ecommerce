import os
from pydantic_settings import SettingsConfigDict, BaseSettings

_model_config = SettingsConfigDict(
    env_file=".env", env_ignore_empty=True, extra="ignore"
)


class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST") or ""
    POSTGRESS_PORT: str = os.getenv("POSTGRESS_PORT") or ""
    POSTGRESS_DB: str = os.getenv("POSTGRESS_DB") or ""
    POSTGRESS_USER: str = os.getenv("POSTGRESS_USER") or ""
    POSTGRESS_PASSWORD: str = os.getenv("POSTGRESS_PASSWORD") or ""

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.POSTGRESS_USER}:{self.POSTGRESS_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRESS_PORT}/{self.POSTGRESS_DB}"

    model_config = _model_config


db = DatabaseSettings()
print(db.database_url)
