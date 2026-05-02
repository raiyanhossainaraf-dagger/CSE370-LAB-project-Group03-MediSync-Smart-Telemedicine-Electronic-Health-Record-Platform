from pydantic import BaseModel
from typing import Optional


# 🔹 Request (when researcher submits report)
class ReportCreate(BaseModel):
    trial_id: int
    researcher_id: int
    summary: str
    result: str


# 🔹 Response (when fetching report)
class ReportOut(BaseModel):
    report_id: int
    trial_id: int
    researcher_id: int
    summary: str
    result: str
    image: Optional[str]
    status: str

    class Config:
        orm_mode = True