# app/schemas/medication_schema.py

from pydantic import BaseModel

class MedicationCreate(BaseModel):
    trial_id: int
    drug_name: str
    dosage: str
    frequency: str

class MedicationResponse(MedicationCreate):
    medication_id: int

    class Config:
        from_attributes = True