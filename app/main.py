from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db, engine
from sqlalchemy import text

app = FastAPI(title="CAVA Suite API")

@app.get("/")
def read_root():
    return {"message": "Reload is working!"}

# New health check endpoint
@app.get("/db-check")
def check_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "Database connection successful!"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}