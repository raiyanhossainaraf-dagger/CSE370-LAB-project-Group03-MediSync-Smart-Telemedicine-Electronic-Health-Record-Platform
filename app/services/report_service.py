# app/services/report_service.py

from sqlalchemy.orm import Session
from app.models.trial_model import Trial
from app.models.participant_model import Participant
from app.core.constants import SUCCESS

def get_summary_report(db: Session):
    total_trials = db.query(Trial).count()
    total_participants = db.query(Participant).count()

    return {
        "status": SUCCESS,
        "total_trials": total_trials,
        "total_participants": total_participants
    }