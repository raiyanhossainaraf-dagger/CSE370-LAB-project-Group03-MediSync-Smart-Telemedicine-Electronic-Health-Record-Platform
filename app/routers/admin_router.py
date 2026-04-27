from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.enrollment_model import Enrollment
from app.models.participant_model import Participant
from app.models.trial_model import Trial
from app.models.researcher_model import Researcher

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/admin")
def get_admin_dashboard(db: Session = Depends(get_db)):

    data = (
        db.query(
            Participant.name.label("participant"),
            Trial.trial_name.label("trial"),
            Trial.phase.label("phase"),
            Enrollment.status.label("status"),
            Researcher.name.label("researcher")
        )
        .join(Enrollment, Enrollment.participant_id == Participant.participant_id)
        .join(Trial, Trial.trial_id == Enrollment.trial_id)
        .join(Researcher, Researcher.researcher_id == Trial.researcher_id)
        .all()
    )

    return [
        {
            "participant": row.participant,
            "trial": row.trial,
            "phase": row.phase,
            "status": row.status,
            "researcher": row.researcher
        }
        for row in data
    ]