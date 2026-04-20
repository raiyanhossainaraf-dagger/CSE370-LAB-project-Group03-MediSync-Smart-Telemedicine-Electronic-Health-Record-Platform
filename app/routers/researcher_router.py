# app/routers/researcher_router.py

from fastapi import APIRouter
from app.core.roles import RESEARCHER

router = APIRouter(prefix="/researchers", tags=["Researchers"])

@router.get("/")
def researcher_dashboard():
    return {
        "role": RESEARCHER,
        "message": "Welcome Researcher"
    }

@router.get("/trials")
def assigned_trials():
    return {
        "role": RESEARCHER,
        "message": "Researcher trials list"
    }