from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.models.enrollment_model import Enrollment

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


# GET all enrollments
@router.get("/")
def get_enrollments(db: Session = Depends(get_db)):
    return db.query(Enrollment).all()


# APPROVE
@router.post("/approve/{enrollment_id}")
def approve_enrollment(enrollment_id: int, db: Session = Depends(get_db)):

    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if not enrollment:
        return {"message": "Enrollment not found"}

    enrollment.status = "Approved"
    db.commit()

    return {"message": "Enrollment approved"}


# REJECT
@router.post("/reject/{enrollment_id}")
def reject_enrollment(enrollment_id: int, db: Session = Depends(get_db)):

    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if not enrollment:
        return {"message": "Enrollment not found"}

    enrollment.status = "Rejected"
    db.commit()

    return {"message": "Enrollment rejected"}


# PENDING
@router.post("/pending/{enrollment_id}")
def pending_enrollment(enrollment_id: int, db: Session = Depends(get_db)):

    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if not enrollment:
        return {"message": "Enrollment not found"}

    enrollment.status = "Pending"
    db.commit()

    return {"message": "Enrollment set to pending"}