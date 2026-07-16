from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str
    FRONTEND_URL: str

    jwt_secret_key: str
    jwt_algorithm: str = "HS256"

    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7


    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
