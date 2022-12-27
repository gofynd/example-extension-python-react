from aioredis import Redis
from app.config import CONFIG


def parse_url(url: str):
    url: list = url.split("&")
    base_url: str = url.pop(0)
    for options in url:
        if options == "ssl=true":
            base_url = base_url.replace("redis://", "rediss://")
    return base_url


class RedisManager:
    def __new__(cls, *args, **kwargs):
        raise RuntimeError(f"{cls} should not be instantiated")

    CONNECTIONS = {}

    @classmethod
    def get_connection(cls, redis_url: str, **kwargs):

        redis_url = parse_url(redis_url)
        if redis_url not in cls.CONNECTIONS:
            cls.CONNECTIONS[redis_url] = Redis.from_url(redis_url, **kwargs)
        return cls.CONNECTIONS[redis_url]

    @classmethod
    async def close(cls):
        for redis_client in cls.CONNECTIONS.values():
            if redis_client is not None:
                await redis_client.close()


# initialising Redis client
redis_client = RedisManager.get_connection(
  CONFIG.REDIS_CONNECTION_HOST,
  decode_responses=True
)