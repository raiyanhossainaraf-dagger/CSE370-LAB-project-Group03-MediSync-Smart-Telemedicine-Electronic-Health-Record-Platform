from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.models.enrollment_model import Enrollment
from app.models.participant_model import Participant
from app.models.trial_model import Trial
from app.models.researcher_model import Researcher

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/admin")
def admin_dashboard(db: Session = Depends(get_db)):

    results = db.query(
        Enrollment.enrollment_id,
        Trial.trial_id,
        Participant.name,
        Trial.trial_name,
        Trial.phase,
        Enrollment.status,
        Researcher.name
    ).join(Participant, Enrollment.participant_id == Participant.participant_id)\
     .join(Trial, Enrollment.trial_id == Trial.trial_id)\
     .join(Researcher, Trial.researcher_id == Researcher.researcher_id)\
     .all()

    return [
        {
            "enrollment_id": r[0],
            "trial_id": r[1],
            "participant": r[2],
            "trial": r[3],
            "phase": r[4],
            "status": r[5],
            "researcher": r[6]
        }
        for r in results
    ]