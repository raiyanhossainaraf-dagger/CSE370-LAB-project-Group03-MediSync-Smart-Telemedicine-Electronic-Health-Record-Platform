# app/schemas/admin_schema.py

from pydantic import BaseModel

class AdminCreate(BaseModel):
    name: str
    role: str

class AdminResponse(AdminCreate):
    admin_id: int

    class Config:
        from_attributes = True


