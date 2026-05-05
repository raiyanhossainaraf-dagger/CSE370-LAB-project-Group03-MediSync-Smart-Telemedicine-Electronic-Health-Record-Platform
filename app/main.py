# =========================
# app/main.py
# =========================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.utils.database import Base, engine


# =========================
# CREATE APP
# =========================
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


# =========================
# CORS CONFIG (Frontend ↔ Backend)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# IMPORT MODELS (VERY IMPORTANT)
# =========================
from app.models import (
    admin_model,
    researcher_model,
    participant_model,
    trial_model,
    eligibility_model,
    enrollment_model,
    medication_model,
    observation_model,
    side_effect_model,
    report_model   # ✅ FIX (you forgot this)
)


# =========================
# CREATE TABLES
# =========================
Base.metadata.create_all(bind=engine)


# =========================
# IMPORT ROUTERS
# =========================
from app.routers import (
    auth_router,
    admin_router,
    participant_router,
    researcher_router,
    trial_router,
    enrollment_router,
    report_router,
    side_effect_router,
    dashboard_router
)


# =========================
# REGISTER ROUTERS
# =========================
app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(participant_router.router)
app.include_router(researcher_router.router)
app.include_router(trial_router.router)
app.include_router(enrollment_router.router)
app.include_router(report_router.router)
app.include_router(side_effect_router.router)
app.include_router(dashboard_router.router)


# =========================
# ROOT ENDPOINT
# =========================
@app.get("/")
def home():
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Backend running successfully"
    }