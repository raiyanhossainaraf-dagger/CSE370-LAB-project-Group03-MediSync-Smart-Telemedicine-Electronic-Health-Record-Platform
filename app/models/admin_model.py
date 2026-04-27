from sqlalchemy import Column, Integer, String
from app.utils.database import Base

class AdminSponsor(Base):
    __tablename__ = "admin_sponsor"

    admin_id = Column(Integer, primary_key=True)
    name = Column(String)