# app/routers/trial_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.dependencies import get_db
from app.models.trial_model import Trial
from app.schemas.trial_schema import TrialCreate
from app.core.constants import ACTIVE

router = APIRouter(prefix="/trials", tags=["Trials"])

@router.get("/")
def get_trials(db: Session = Depends(get_db)):
    return db.query(Trial).all()

@router.post("/")
def create_trial(trial: TrialCreate, db: Session = Depends(get_db)):
    new_trial = Trial(**trial.model_dump())
    db.add(new_trial)
    db.commit()
    db.refresh(new_trial)

    return {
        "status": ACTIVE,
        "data": new_trial
    }

from fastapi import HTTPException

@router.delete("/{trial_id}")
def delete_trial(trial_id: int, db: Session = Depends(get_db)):

    trial = db.query(Trial).filter(Trial.trial_id == trial_id).first()

    if not trial:
        raise HTTPException(status_code=404, detail="Trial not found")

    db.delete(trial)
    db.commit()

    return {"message": f"Trial {trial_id} deleted successfully"}