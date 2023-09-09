from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    login: str
    password: str
    bstack_user: str
    bstack_key: str
    bstack_url: str

    class Config:
        env_file = ".env"


settings = Settings()