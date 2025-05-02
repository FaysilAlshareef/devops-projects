from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/db-health")
async def check_db_connection(db: Session = Depends(get_db)):
    try:
        # Execute a simple query to check database connection
        result = db.execute(text("SELECT 1"))
        if result.scalar() == 1:
            return JSONResponse(
                content={
                    "status": "healthy",
                    "message": "Database connection is working properly"
                },
                status_code=200
            )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database connection failed: {str(e)}"
        )