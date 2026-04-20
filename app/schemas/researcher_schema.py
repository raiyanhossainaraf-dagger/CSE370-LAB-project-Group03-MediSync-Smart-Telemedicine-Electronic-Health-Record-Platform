# app/schemas/researcher_schema.py

from pydantic import BaseModel

class ResearcherCreate(BaseModel):
    name: str
    specialization: str
    contact: str
    email: str

class ResearcherResponse(ResearcherCreate):
    researcher_id: int

    class Config:
        from_attributes = True