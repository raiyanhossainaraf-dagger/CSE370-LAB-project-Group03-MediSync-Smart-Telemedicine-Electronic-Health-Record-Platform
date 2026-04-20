# app/routers/admin_router.py

from fastapi import APIRouter
from app.core.roles import ADMIN

router = APIRouter(prefix="/admins", tags=["Admins"])

@router.get("/")
def get_admin_dashboard():
    return {
        "role": ADMIN,
        "message": "Welcome to Admin Dashboard"
    }

@router.post("/create")
def create_admin():
    return {
        "role": ADMIN,
        "message": "Admin created successfully"
    }