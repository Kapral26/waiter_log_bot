from pathlib import Path

from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

dotenv_path = Path(__file__).parent.absolute() / ".env"


class Settings(BaseSettings):
    """Pydantic settings."""

    bot_token: SecretStr = Field(..., alias="BOT_TOKEN")
    pg_host: str = Field(..., alias="POSTGRES_HOST")
    pg_port: int = Field(..., alias="POSTGRES_PORT")

    pg_login: str = Field(..., alias="POSTGRES_USER")
    pg_pass: SecretStr = Field(..., alias="POSTGRES_PASSWORD")

    pg_dbname: str = Field(..., alias="POSTGRES_DB")

    db_echo: bool = Field(..., alias="DB_ECHO")
    db_pool_size: int = Field(..., alias="DB_POOL_SIZE")
    db_max_overflow: int = Field(..., alias="DB_MAX_OVERFLOW")

    model_config = SettingsConfigDict(
            env_file=dotenv_path,
            env_file_encoding="utf-8"
    )


if __name__ == "__main__":
    # При импорте файла сразу создастся
    # и провалидируется объект конфига,
    # который можно далее импортировать из разных мест
    settings = Settings()
