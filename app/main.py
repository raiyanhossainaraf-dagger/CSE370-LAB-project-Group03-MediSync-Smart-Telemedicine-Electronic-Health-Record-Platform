from fastapi import FastAPI
from app.utils.database import Base, engine

from app.models import researcher_model
from app.models import participant_model
from app.models import trial_model

from app.routers import trial_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clinical Trial Management System")

app.include_router(trial_router.router)

@app.get("/")
def home():
    return {"message": "Clinical Trial API Running"}