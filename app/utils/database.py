# app/utils/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

# Create MySQL / MariaDB Engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)

# Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base Class for Models
Base = declarative_base()