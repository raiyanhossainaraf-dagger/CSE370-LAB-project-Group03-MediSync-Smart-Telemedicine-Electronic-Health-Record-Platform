# app/services/trial_service.py

from sqlalchemy.orm import Session
from app.models.trial_model import Trial

def get_all_trials(db: Session):
    return db.query(Trial).all()

def create_trial(db: Session, data):
    new_trial = Trial(**data.model_dump())
    db.add(new_trial)
    db.commit()
    db.refresh(new_trial)
    return new_trial