from fastapi import APIRouter, HTTPException
import redis
from fastapi.responses import JSONResponse
from ...core.config import settings

router = APIRouter()

def get_redis_client():
    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        decode_responses=True
    )

@router.get("/redis-health")
async def check_redis_connection():
    try:
        redis_client = get_redis_client()
        # Test Redis by setting and getting a value
        redis_client.set("health_check", "ok")
        result = redis_client.get("health_check")
        redis_client.delete("health_check")
        
        if result == "ok":
            return JSONResponse(
                content={
                    "status": "healthy",
                    "message": "Redis connection is working properly"
                },
                status_code=200
            )
    except redis.ConnectionError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Redis connection failed: {str(e)}"
        )