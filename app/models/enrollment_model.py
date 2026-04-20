# app/models/enrollment_model.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.utils.database import Base

class Enrollment(Base):
    __tablename__ = "enrollment"

    enrollment_id = Column(Integer, primary_key=True, index=True)
    trial_id = Column(Integer, ForeignKey("trial.trial_id"))
    participant_id = Column(Integer, ForeignKey("participant.participant_id"))

    enrollment_date = Column(Date)
    status = Column(String(30))