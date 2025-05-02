from fastapi import FastAPI
from app.api.endpoints import hello, db_check, redis_check
from app.core.config import settings

app = FastAPI()

# Include the API routes
app.include_router(hello.router)
app.include_router(db_check.router)
app.include_router(redis_check.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the FastAPI app!",
        "database_url": settings.DATABASE_URL,
        "redis_url": settings.REDIS_URL,
    }