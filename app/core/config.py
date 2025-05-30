from pydantic_settings import BaseSettings

class Env(BaseSettings):
    DATABASE_URL: str
    ALGORITHM: str = "HS256"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

env = Env()