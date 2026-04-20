# app/models/side_effect_model.py

from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.database import Base

class SideEffect(Base):
    __tablename__ = "side_effect"

    effect_id = Column(Integer, primary_key=True, index=True)
    trial_id = Column(Integer, ForeignKey("trial.trial_id"))

    effect_type = Column(String(100))
    severity = Column(String(20))
    duration = Column(Integer)