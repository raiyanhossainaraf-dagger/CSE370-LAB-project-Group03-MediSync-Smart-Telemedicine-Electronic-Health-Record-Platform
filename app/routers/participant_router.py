# app/routers/participant_router.py

from fastapi import APIRouter
from app.core.roles import PARTICIPANT

router = APIRouter(prefix="/participants", tags=["Participants"])

@router.get("/")
def participant_dashboard():
    return {
        "role": PARTICIPANT,
        "message": "Welcome Participant"
    }

@router.get("/profile")
def profile():
    return {
        "role": PARTICIPANT,
        "message": "Participant profile"
    }