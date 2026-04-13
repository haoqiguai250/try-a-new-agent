from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ARK_API_KEY: str
    ARK_BASE_URL: str = "https://ark.cn-beijing.volces.com/api/v3"
    ARK_MODEL: str = "doubao-seed-2-0-lite-260215"

    class Config:
        env_file = ".env"

settings = Settings()