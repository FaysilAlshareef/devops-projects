from fastapi import APIRouter
from .endpoints import hello, db_check, redis_check

# Create the main API router
api_router = APIRouter()

# Include routers from endpoints
api_router.include_router(hello.router, tags=["hello"])
api_router.include_router(db_check.router, tags=["database"])
api_router.include_router(redis_check.router, tags=["redis"])