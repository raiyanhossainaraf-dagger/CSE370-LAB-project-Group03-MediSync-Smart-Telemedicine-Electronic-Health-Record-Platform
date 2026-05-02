from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.database import Base


class SideEffect(Base):
    __tablename__ = "side_effect"

    effect_id = Column(Integer, primary_key=True, index=True)
    trial_id = Column(Integer, ForeignKey("trial.trial_id"))
    participant_id = Column(Integer, ForeignKey("participant.participant_id"))  # ✅ NEW

    effect_type = Column(String(100))
    severity = Column(String(20))
    duration = Column(Integer)