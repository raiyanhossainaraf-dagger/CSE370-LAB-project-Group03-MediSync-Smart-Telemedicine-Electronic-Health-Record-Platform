# app/services/researcher_service.py

from sqlalchemy.orm import Session
from app.models.researcher_model import Researcher

def get_all_researchers(db: Session):
    return db.query(Researcher).all()

def create_researcher(db: Session, data):
    new_researcher = Researcher(**data.model_dump())
    db.add(new_researcher)
    db.commit()
    db.refresh(new_researcher)
    return new_researcher