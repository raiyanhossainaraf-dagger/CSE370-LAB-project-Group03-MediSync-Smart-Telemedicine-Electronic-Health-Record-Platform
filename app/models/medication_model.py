# app/models/medication_model.py

from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.database import Base

class Medication(Base):
    __tablename__ = "medication"

    medication_id = Column(Integer, primary_key=True, index=True)
    trial_id = Column(Integer, ForeignKey("trial.trial_id"))

    drug_name = Column(String(100))
    dosage = Column(String(50))
    frequency = Column(String(50))