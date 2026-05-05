from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.models.report_model import Report
from app.models.trial_model import Trial
from app.models.participant_model import Participant

from app.schemas.report_schema import ReportCreate, ReportOut

router = APIRouter(prefix="/dashboard", tags=["Researcher"])


# ================= PUBLISH REPORT =================
@router.post("/report")
def submit_report(data: ReportCreate, db: Session = Depends(get_db)):

    report = Report(
        trial_id=data.trial_id,
        researcher_id=data.researcher_id,
        summary=data.summary,
        result=data.result,
        status="Published"
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return {"message": "Report published", "report_id": report.report_id}


# ================= GET ALL REPORTS =================
@router.get("/reports")
def get_all_reports(db: Session = Depends(get_db)):
    reports = db.query(Report).all()

    return [
        {
            "report_id": r.report_id,
            "trial_id": r.trial_id,
            "researcher_id": r.researcher_id,
            "summary": r.summary,
            "result": r.result,
            "status": r.status,
            "created_at": r.created_at
        }
        for r in reports
    ]


# ================= GET REPORTS BY RESEARCHER =================
@router.get("/reports/researcher/{researcher_id}", response_model=list[ReportOut])
def get_reports_by_researcher(researcher_id: int, db: Session = Depends(get_db)):
    return (
        db.query(Report)
        .filter(Report.researcher_id == researcher_id)
        .order_by(Report.created_at.desc())
        .all()
    )


# ================= DASHBOARD SUMMARY =================
@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total_trials = db.query(Trial).count()
    total_participants = db.query(Participant).count()

    return {
        "total_trials": total_trials,
        "total_participants": total_participants
    }