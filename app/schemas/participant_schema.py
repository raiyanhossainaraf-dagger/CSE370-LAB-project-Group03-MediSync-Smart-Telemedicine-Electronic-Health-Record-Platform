# app/schemas/participant_schema.py

from pydantic import BaseModel

class ParticipantCreate(BaseModel):
    name: str
    age: int
    gender: str
    medical_history: str
    allergy_info: str

class ParticipantResponse(ParticipantCreate):
    participant_id: int

    class Config:
        from_attributes = True