# app/main.py

from fastapi import FastAPI

from app.config import settings
from app.utils.database import Base, engine

# Import all models
from app.models import admin_model
from app.models import researcher_model
from app.models import participant_model
from app.models import trial_model
from app.models import eligibility_model
from app.models import enrollment_model
from app.models import medication_model
from app.models import observation_model
from app.models import side_effect_model

# Import all routers
from app.routers import (
    auth_router,
    admin_router,
    participant_router,
    researcher_router,
    trial_router,
    enrollment_router,
    report_router
)

# Create tables automatically
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Include routers
app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(participant_router.router)
app.include_router(researcher_router.router)
app.include_router(trial_router.router)
app.include_router(enrollment_router.router)
app.include_router(report_router.router)

# Home Route
@app.get("/")
def home():
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION
    }