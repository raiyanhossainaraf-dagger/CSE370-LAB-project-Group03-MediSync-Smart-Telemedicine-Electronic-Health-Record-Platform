from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.models.enrollment_model import Enrollment
from app.models.trial_model import Trial
from app.models.medication_model import Medication
from app.models.observation_model import Observation

router = APIRouter(prefix="/dashboard", tags=["Participant"])


# ================= DASHBOARD =================
@router.get("/participant/{participant_id}")
def participant_dashboard(participant_id: int, db: Session = Depends(get_db)):

    results = (
        db.query(
            Trial.trial_name,
            Trial.phase,
            Enrollment.status
        )
        .join(Enrollment, Enrollment.trial_id == Trial.trial_id)
        .filter(Enrollment.participant_id == participant_id)
        .all()
    )

    return [
        {"trial": r[0], "phase": r[1], "status": r[2]}
        for r in results
    ]


# ================= MEDICATION =================
@router.get("/medication/{participant_id}")
def get_medications(participant_id: int, db: Session = Depends(get_db)):

    results = (
        db.query(
            Medication.drug_name,
            Medication.dosage,
            Medication.frequency
        )
        .join(Trial, Trial.trial_id == Medication.trial_id)
        .join(Enrollment, Enrollment.trial_id == Trial.trial_id)
        .filter(Enrollment.participant_id == participant_id)
        .all()
    )

    return [
        {"drug_name": r[0], "dosage": r[1], "frequency": r[2]}
        for r in results
    ]


# ================= VISIT SCHEDULE =================
@router.get("/schedule/{participant_id}")
def get_schedule(participant_id: int, db: Session = Depends(get_db)):

    results = (
        db.query(
            Trial.trial_name,
            Observation.visit_date,
            Observation.notes
        )
        .join(Observation, Observation.trial_id == Trial.trial_id)
        .filter(Observation.participant_id == participant_id)
        .all()
    )

    return [
        {
            "trial": r[0],
            "visit_date": str(r[1]),
            "notes": r[2]
        }
        for r in results
    ]