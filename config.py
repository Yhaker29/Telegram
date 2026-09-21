from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TOKEN: str
    ADMIN_ID: int

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
