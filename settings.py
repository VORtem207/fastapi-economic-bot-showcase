from dotenv import load_dotenv

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    db_password: str
    db_host: str
    db_username: str
    db_name: str
    db_port: int


settings = Settings()


if __name__ == "__main__":
    print("📦 Loaded settings:")
    for key, value in settings.model_dump().items():
        masked = "***" if "secret" in key or "password" in key else value
        print(f"  {key}: {masked}")
