from pydantic import BaseModel
from datetime import datetime


class ReportCreate(BaseModel):
    trial_id: int
    researcher_id: int
    summary: str
    result: str


class ReportOut(BaseModel):
    report_id: int
    trial_id: int
    researcher_id: int
    summary: str
    result: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True