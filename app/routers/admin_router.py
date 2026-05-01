from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.models.enrollment_model import Enrollment
from app.models.participant_model import Participant
from app.models.trial_model import Trial
from app.models.researcher_model import Researcher

router = APIRouter(prefix="/admin", tags=["Admin"])


# ================= ADMIN DASHBOARD (OPTIONAL) =================
@router.get("/info")
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


# ================= CREATE TRIAL =================
@router.post("/create-trial")
def create_trial(data: dict, db: Session = Depends(get_db)):

    trial_name = data.get("trial_name")
    phase = data.get("phase")
    researcher_id = data.get("researcher_id")
    participant_ids = data.get("participants", [])

    researcher = db.query(Researcher).filter(
        Researcher.researcher_id == researcher_id
    ).first()

    if not researcher:
        raise HTTPException(status_code=404, detail="Researcher not found")

    new_trial = Trial(
        trial_name=trial_name,
        phase=phase,
        researcher_id=researcher_id
    )

    db.add(new_trial)
    db.commit()
    db.refresh(new_trial)

    # Create enrollments
    for pid in participant_ids:
        participant = db.query(Participant).filter(
            Participant.participant_id == pid
        ).first()

        if participant:
            enrollment = Enrollment(
                participant_id=pid,
                trial_id=new_trial.trial_id,
                status="Pending"
            )
            db.add(enrollment)

    db.commit()

    return {"message": "Trial created successfully"}


# ================= DELETE TRIAL =================
@router.delete("/delete-trial/{trial_id}")
def delete_trial(trial_id: int, db: Session = Depends(get_db)):

    trial = db.query(Trial).filter(Trial.trial_id == trial_id).first()

    if not trial:
        raise HTTPException(status_code=404, detail="Trial not found")

    # Delete related enrollments first
    db.query(Enrollment).filter(Enrollment.trial_id == trial_id).delete()

    db.delete(trial)
    db.commit()

    return {"message": "Trial deleted"}


# ================= GET ALL RESEARCHERS =================
@router.get("/researchers")
def get_researchers(db: Session = Depends(get_db)):
    data = db.query(Researcher).all()

    return [
        {
            "id": r.researcher_id,
            "name": r.name,
            "specialization": r.specialization,
            "email": r.email
        }
        for r in data
    ]


# ================= GET ALL PARTICIPANTS =================
@router.get("/participants")
def get_participants(db: Session = Depends(get_db)):
    data = db.query(Participant).all()

    return [
        {
            "id": p.participant_id,
            "name": p.name,
            "age": p.age,
            "gender": p.gender,
            "medical_history": p.medical_history
        }
        for p in data
    ]