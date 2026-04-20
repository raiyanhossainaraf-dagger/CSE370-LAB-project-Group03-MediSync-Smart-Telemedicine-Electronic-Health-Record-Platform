# app/routers/report_router.py

from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/summary")
def report_summary():
    return {
        "total_trials": 2,
        "total_participants": 10,
        "active_trials": 1
    }