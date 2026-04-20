# app/schemas/side_effect_schema.py

from pydantic import BaseModel

class SideEffectCreate(BaseModel):
    trial_id: int
    effect_type: str
    severity: str
    duration: int

class SideEffectResponse(SideEffectCreate):
    effect_id: int

    class Config:
        from_attributes = True