# app/models/researcher_model.py

from sqlalchemy import Column, Integer, String
from app.utils.database import Base

class Researcher(Base):
    __tablename__ = "researcher"

    researcher_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100))
    contact = Column(String(20))
    email = Column(String(100), unique=True)