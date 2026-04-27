from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.models.enrollment_model import Enrollment

router = APIRouter(prefix="/participants", tags=["Participants"])


@router.get("/enrolled/{participant_id}")
def get_enrolled_trials(participant_id: int, db: Session = Depends(get_db)):
    enrollments = db.query(Enrollment).filter(
        Enrollment.participant_id == participant_id
    ).all()

    return enrollments