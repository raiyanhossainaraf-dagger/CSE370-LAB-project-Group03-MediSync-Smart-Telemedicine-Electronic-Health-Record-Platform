from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.models.researcher_model import Researcher
from app.models.admin_model import AdminSponsor
from app.models.participant_model import Participant

from app.schemas.auth_schema import LoginRequest, LoginResponse

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):

    # ================= ADMIN =================
    admin = db.query(AdminSponsor).filter(
        AdminSponsor.name == data.username,
        AdminSponsor.password == data.password
    ).first()

    if admin:
        return {
            "role": "admin",
            "user_id": admin.admin_id,
            "name": admin.name
        }

    # ================= RESEARCHER =================
    researcher = db.query(Researcher).filter(
        Researcher.name == data.username,
        Researcher.password == data.password
    ).first()

    if researcher:
        return {
            "role": "researcher",
            "user_id": researcher.researcher_id,
            "name": researcher.name
        }

    # ================= PARTICIPANT =================
    participant = db.query(Participant).filter(
        Participant.name == data.username,
        Participant.password == data.password
    ).first()

    if participant:
        return {
            "role": "participant",
            "user_id": participant.participant_id,
            "name": participant.name
        }

    # ================= INVALID =================
    raise HTTPException(status_code=401, detail="Invalid credentials")