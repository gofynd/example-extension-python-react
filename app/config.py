import os
from pydantic import BaseSettings

class Config(BaseSettings):

    ENV: str = "prod"
    SERVER_TYPE: str = "dev"
    DEBUG: str = "true"

    REDIS_CONNECTION_HOST: str = "redis://localhost:6379/0"

    PORT: int
    EXTENSION_API_KEY: str
    EXTENSION_API_SECRET: str
    EXTENSION_BASE_URL: str
    EXTENSION_CLUSTER_URL: str

    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

    class Config:
        env_file=".env"


CONFIG = Config()
