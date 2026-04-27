from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.models.trial_model import Trial
from app.models.participant_model import Participant

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total_trials = db.query(Trial).count()
    total_participants = db.query(Participant).count()

    return {
        "total_trials": total_trials,
        "total_participants": total_participants
    }