from pydantic import BaseModel
from datetime import date

class TrialCreate(BaseModel):
    trial_name: str
    drug_name: str
    phase: str
    start_date: date
    end_date: date
    duration: int
    researcher_id: int
    admin_id: int

class TrialResponse(TrialCreate):
    trial_id: int

    class Config:
        orm_mode = True