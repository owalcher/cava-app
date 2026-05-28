import os
# from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# env_path = Path(__file__).resolve().parent.parent.parent / ".env"
# load_dotenv(dotenv_path=env_path)
# rint(f"DEBUG: Looking for .env at: {env_path}")
# print(f"DEBUG: File exists: {env_path.exists()}")
# print(f"DEBUG: Environment variable DATABASE_URL is: {os.getenv('DATABASE_URL')}")

# We'll put the connection string in your .env file
# owen changes next line from
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/cava_db")
# to
# 1. Load .env only if we are in a local development environment
# This is a safe check: if we are on a server, this file won't exist anyway.
if os.getenv("ENVIRONMENT") != "production":
    load_dotenv()

# 2. Always pull from os.environ. The system will handle whether 
# it comes from the .env file (local) or the server settings (production).
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL must be set in your environment!")


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get a DB session in our routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()