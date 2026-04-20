# app/models/observation_model.py

from sqlalchemy import Column, Integer, String, Date, Text, DECIMAL, ForeignKey
from app.utils.database import Base

class Observation(Base):
    __tablename__ = "observation"

    observation_id = Column(Integer, primary_key=True, index=True)
    trial_id = Column(Integer, ForeignKey("trial.trial_id"))
    participant_id = Column(Integer, ForeignKey("participant.participant_id"))

    visit_date = Column(Date)
    blood_pressure = Column(String(20))
    temperature = Column(DECIMAL(4,1))
    notes = Column(Text)