from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.models.admin_model import AdminSponsor
from app.models.researcher_model import Researcher
from app.models.participant_model import Participant

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):

    username = data.get("username")

    # Check Admin
    admin = db.query(AdminSponsor).filter(AdminSponsor.name == username).first()

    if admin:
        return {
            "role": "admin",
            "user_id": admin.admin_id,
            "name": admin.name
        }

    # Check Researcher
    researcher = db.query(Researcher).filter(Researcher.name == username).first()
    if researcher:
        return {
            "role": "researcher",
            "user_id": researcher.researcher_id,
            "name": researcher.name
        }

    # Check Participant
    participant = db.query(Participant).filter(Participant.name == username).first()
    if participant:
        return {
            "role": "participant",
            "user_id": participant.participant_id,
            "name": participant.name
        }

    raise HTTPException(status_code=401, detail="Invalid user")