# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.utils.database import Base, engine

# =========================
# Import all models
# =========================
from app.models import admin_model
from app.models import researcher_model
from app.models import participant_model
from app.models import trial_model
from app.models import eligibility_model
from app.models import enrollment_model
from app.models import medication_model
from app.models import observation_model
from app.models import side_effect_model

# =========================
# Import all routers
# =========================
from app.routers import (
    auth_router,
    admin_router,
    participant_router,
    researcher_router,
    trial_router,
    enrollment_router,
    report_router,
    side_effect_router
)

# =========================
# Create FastAPI App
# =========================
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# =========================
# Enable CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Create Database Tables
# =========================
Base.metadata.create_all(bind=engine)

# =========================
# Include Routers
# =========================
app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(participant_router.router)
app.include_router(researcher_router.router)
app.include_router(trial_router.router)
app.include_router(enrollment_router.router)
app.include_router(report_router.router)
app.include_router(side_effect_router.router)

# =========================
# Root Route
# =========================
@app.get("/")
def home():
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running Successfully"
    }