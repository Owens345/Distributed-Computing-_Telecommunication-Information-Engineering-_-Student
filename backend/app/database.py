# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Connection URL to PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:MyStrongPassword123@localhost:5432/lease_system"

# Engine represents the core DB connection pool
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL queries

# Session factory for creating database sessions (transactions)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Dependency function for FastAPI endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()