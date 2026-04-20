# app/schemas/enrollment_schema.py

from pydantic import BaseModel
from datetime import date

class EnrollmentCreate(BaseModel):
    trial_id: int
    participant_id: int
    enrollment_date: date
    status: str

class EnrollmentResponse(EnrollmentCreate):
    enrollment_id: int

    class Config:
        from_attributes = True