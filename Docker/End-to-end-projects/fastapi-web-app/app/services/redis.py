import redis
from fastapi import HTTPException
from app.core.config import settings

class RedisService:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )

    def check_connection(self):
        try:
            return self.client.ping()
        except redis.ConnectionError:
            raise HTTPException(status_code=500, detail="Redis connection failed")

    def set_value(self, key: str, value: str, expiration: int = 3600):
        try:
            self.client.set(key, value, ex=expiration)
        except redis.RedisError as e:
            raise HTTPException(status_code=500, detail=f"Failed to set value in Redis: {str(e)}")

    def get_value(self, key: str):
        try:
            value = self.client.get(key)
            if value is None:
                raise HTTPException(status_code=404, detail="Key not found")
            return value
        except redis.RedisError as e:
            raise HTTPException(status_code=500, detail=f"Failed to get value from Redis: {str(e)}")