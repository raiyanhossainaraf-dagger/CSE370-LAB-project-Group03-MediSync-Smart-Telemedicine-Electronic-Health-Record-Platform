from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.utils.database import Base

class Trial(Base):
    __tablename__ = "trial"

    trial_id = Column(Integer, primary_key=True, index=True)
    trial_name = Column(String(150))
    drug_name = Column(String(100))
    phase = Column(String(20))
    start_date = Column(Date)
    end_date = Column(Date)
    duration = Column(Integer)

    researcher_id = Column(Integer, ForeignKey("researcher.researcher_id"))
    admin_id = Column(Integer, ForeignKey("admin_sponsor.admin_id"))