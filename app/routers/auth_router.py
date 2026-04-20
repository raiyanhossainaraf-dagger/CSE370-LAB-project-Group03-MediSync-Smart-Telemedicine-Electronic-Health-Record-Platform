# app/routers/auth_router.py

from fastapi import APIRouter
from app.core.roles import ADMIN, RESEARCHER, PARTICIPANT
from app.schemas.user_schema import UserLogin

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login(user: UserLogin):
    if user.username == "admin":
        return {
            "message": "Login successful",
            "role": ADMIN
        }

    elif user.username == "researcher":
        return {
            "message": "Login successful",
            "role": RESEARCHER
        }

    elif user.username == "participant":
        return {
            "message": "Login successful",
            "role": PARTICIPANT
        }

    return {
        "message": "Invalid credentials"
    }


@router.post("/logout")
def logout():
    return {"message": "Logout successful"}