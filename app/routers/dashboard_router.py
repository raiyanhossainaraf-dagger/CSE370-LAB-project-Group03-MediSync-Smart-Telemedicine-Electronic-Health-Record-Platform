from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.models.trial_model import Trial
from app.models.participant_model import Participant
from app.models.enrollment_model import Enrollment
from app.models.researcher_model import Researcher

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


# ================= ADMIN =================
@router.get("/admin")
def admin_dashboard(db: Session = Depends(get_db)):

    results = db.query(
        Enrollment.enrollment_id,
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
            "participant_name": r[1],
            "trial_name": r[2],
            "phase": r[3],
            "status": r[4],
            "researcher_name": r[5]
        }
        for r in results
    ]


# ================= RESEARCHER =================
@router.get("/researcher/{researcher_id}")
def researcher_dashboard(researcher_id: int, db: Session = Depends(get_db)):

    results = db.query(
        Trial.trial_name,
        Trial.phase,
        Participant.name,
        Participant.age,
        Participant.gender,
        Enrollment.status
    ).join(Enrollment, Trial.trial_id == Enrollment.trial_id)\
     .join(Participant, Enrollment.participant_id == Participant.participant_id)\
     .filter(Trial.researcher_id == researcher_id)\
     .all()

    return [
        {
            "trial_name": r[0],
            "phase": r[1],
            "participant_name": r[2],
            "age": r[3],
            "gender": r[4],
            "status": r[5]
        }
        for r in results
    ]


# ================= PARTICIPANT =================
@router.get("/participant/{participant_id}")
def participant_dashboard(participant_id: int, db: Session = Depends(get_db)):

    results = db.query(
        Trial.trial_name,
        Trial.phase,
        Enrollment.status
    ).join(Enrollment, Trial.trial_id == Enrollment.trial_id)\
     .filter(Enrollment.participant_id == participant_id)\
     .all()

    return [
        {
            "trial_name": r[0],
            "phase": r[1],
            "status": r[2]
        }
        for r in results
    ]