# app/models/participant_model.py

from sqlalchemy import Column, Integer, String, Text
from app.utils.database import Base

class Participant(Base):
    __tablename__ = "participant"

    participant_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    gender = Column(String(10))
    medical_history = Column(Text)