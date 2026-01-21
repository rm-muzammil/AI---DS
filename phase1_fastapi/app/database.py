from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import Depends
import os

# DATABASE_URL = "postgresql://postgres:postGRE@localhost:5432/phase1_db"
DATABASE_URL = os.getenv("DATABASE_URL","postgresql://postgres:postGRE@localhost:5432/phase1_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()