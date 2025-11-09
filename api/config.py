from pydantic_settings import BaseSettings, SettingsConfigDict

# Environment Variables


class Settings(
    BaseSettings,
):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    jwt_secret: str


settings = Settings()
