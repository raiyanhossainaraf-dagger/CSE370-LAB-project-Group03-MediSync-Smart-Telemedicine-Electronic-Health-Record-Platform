from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.models.enrollment_model import Enrollment

router = APIRouter(prefix="/enrollment", tags=["Enrollment"])


# ================= APPLY FOR TRIAL =================
@router.post("/apply")
def apply_trial(data: dict, db: Session = Depends(get_db)):

    # prevent duplicate
    existing = db.query(Enrollment).filter(
        Enrollment.participant_id == data["participant_id"],
        Enrollment.trial_id == data["trial_id"]
    ).first()

    if existing:
        return {"message": "Already applied"}

    new_enrollment = Enrollment(
        participant_id=data["participant_id"],
        trial_id=data["trial_id"],
        status="Pending"
    )

    db.add(new_enrollment)
    db.commit()

    return {"message": "Applied successfully"}


# ================= GET ALL =================
@router.get("/")
def get_enrollments(db: Session = Depends(get_db)):
    return db.query(Enrollment).all()


# ================= APPROVE =================
@router.put("/approve/{enrollment_id}")
def approve_enrollment(enrollment_id: int, db: Session = Depends(get_db)):

    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(status_code=404, detail="Not found")

    enrollment.status = "Approved"
    db.commit()

    return {"message": "Approved"}


# ================= REJECT =================
@router.put("/reject/{enrollment_id}")
def reject_enrollment(enrollment_id: int, db: Session = Depends(get_db)):

    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(status_code=404, detail="Not found")

    enrollment.status = "Rejected"
    db.commit()

    return {"message": "Rejected"}


# ================= DELETE =================
@router.delete("/delete/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):

    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(enrollment)
    db.commit()

    return {"message": "Deleted"}