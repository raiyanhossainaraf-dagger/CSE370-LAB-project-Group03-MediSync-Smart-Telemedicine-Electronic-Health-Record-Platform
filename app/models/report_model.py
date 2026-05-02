from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime

from app.utils.database import Base


class Report(Base):
    __tablename__ = "report"

    report_id = Column(Integer, primary_key=True, index=True)

    # Relations
    trial_id = Column(Integer, ForeignKey("trial.trial_id"), nullable=False)
    researcher_id = Column(Integer, ForeignKey("researcher.researcher_id"), nullable=False)

    # Content
    summary = Column(Text, nullable=False)
    result = Column(Text, nullable=False)

    # Optional image path (admin can attach later)
    image = Column(String(255), nullable=True)

    # Status for admin approval
    status = Column(String(20), default="Pending")

    # Timestamp
    created_at = Column(DateTime, default=datetime.utcnow)