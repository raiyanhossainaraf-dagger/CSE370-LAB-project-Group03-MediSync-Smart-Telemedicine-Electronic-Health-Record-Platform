# app/schemas/observation_schema.py

from pydantic import BaseModel
from datetime import date

class ObservationCreate(BaseModel):
    trial_id: int
    participant_id: int
    visit_date: date
    blood_pressure: str
    temperature: float
    notes: str

class ObservationResponse(ObservationCreate):
    observation_id: int

    class Config:
        from_attributes = True