# app/schemas/eligibility_schema.py

from pydantic import BaseModel

class EligibilityCreate(BaseModel):
    trial_id: int
    min_age: int
    max_age: int
    required_condition: str
    exclusions: str

class EligibilityResponse(EligibilityCreate):
    criteria_id: int

    class Config:
        from_attributes = True