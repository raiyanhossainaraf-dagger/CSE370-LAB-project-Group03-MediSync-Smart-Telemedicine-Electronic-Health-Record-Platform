# app/routers/enrollment_router.py

from fastapi import APIRouter
from app.core.constants import APPROVED, PENDING, REJECTED

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.get("/")
def get_enrollments():
    return {
        "message": "Enrollment list"
    }

@router.post("/approve")
def approve_enrollment():
    return {
        "status": APPROVED
    }

@router.post("/pending")
def pending_enrollment():
    return {
        "status": PENDING
    }

@router.post("/reject")
def reject_enrollment():
    return {
        "status": REJECTED
    }