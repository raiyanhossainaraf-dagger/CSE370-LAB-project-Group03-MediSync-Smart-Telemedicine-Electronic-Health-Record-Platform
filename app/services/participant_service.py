# app/services/participant_service.py

from sqlalchemy.orm import Session
from app.models.participant_model import Participant

def get_all_participants(db: Session):
    return db.query(Participant).all()

def create_participant(db: Session, data):
    new_participant = Participant(**data.model_dump())
    db.add(new_participant)
    db.commit()
    db.refresh(new_participant)
    return new_participant