# app/models/eligibility_model.py

from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.database import Base

class EligibilityCriteria(Base):
    __tablename__ = "eligibility_criteria"

    criteria_id = Column(Integer, primary_key=True, index=True)
    trial_id = Column(Integer, ForeignKey("trial.trial_id"))

    min_age = Column(Integer)
    max_age = Column(Integer)
    required_condition = Column(String(100))
    exclusions = Column(String(255))