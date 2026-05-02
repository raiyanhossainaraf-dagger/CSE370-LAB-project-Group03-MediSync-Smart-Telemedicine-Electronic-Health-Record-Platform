from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.models.trial_model import Trial
from app.models.enrollment_model import Enrollment
from app.models.participant_model import Participant
from app.models.side_effect_model import SideEffect
from app.models.observation_model import Observation
from app.models.eligibility_model import EligibilityCriteria
from app.models.report_model import Report
from app.schemas.report_schema import ReportCreate

router = APIRouter(prefix="/dashboard", tags=["Researcher"])


# ================= RESEARCHER DASHBOARD =================
@router.get("/researcher/{researcher_id}")
def researcher_dashboard(researcher_id: int, db: Session = Depends(get_db)):

    results = (
        db.query(
            Trial.trial_name,
            Trial.phase,
            Participant.name,
            Enrollment.status
        )
        .join(Enrollment, Enrollment.trial_id == Trial.trial_id)
        .join(Participant, Participant.participant_id == Enrollment.participant_id)
        .filter(Trial.researcher_id == researcher_id)
        .all()
    )

    return [
        {
            "trial": r[0],
            "phase": r[1],
            "participant": r[2],
            "status": r[3]
        }
        for r in results
    ]


# ================= SIDE EFFECTS (FIXED JOIN) =================
@router.get("/effects/{researcher_id}")
def get_researcher_effects(researcher_id: int, db: Session = Depends(get_db)):

    results = (
        db.query(
            Participant.name,
            Trial.trial_name,
            SideEffect.effect_type,
            SideEffect.severity,
            SideEffect.duration
        )
        .join(Enrollment, Enrollment.participant_id == Participant.participant_id)
        .join(Trial, Trial.trial_id == Enrollment.trial_id)

        .join(SideEffect, SideEffect.trial_id == Trial.trial_id)

        .filter(Trial.researcher_id == researcher_id)
        .all()
    )

    return [
        {
            "participant": r[0],
            "trial": r[1],
            "effect": r[2],
            "severity": r[3],
            "duration": r[4]
        }
        for r in results
    ]

from app.models.medication_model import Medication

@router.post("/medication")
def add_medication(data: dict, db: Session = Depends(get_db)):

    new_med = Medication(
        trial_id=data["trial_id"],
        drug_name=data["drug_name"],
        dosage=data["dosage"],
        frequency=data["frequency"],
        researcher_id=data["researcher_id"]
    )

    db.add(new_med)
    db.commit()

    return {"message": "Medication added"}

@router.post("/observation")
def add_observation(data: dict, db: Session = Depends(get_db)):

    obs = Observation(
        trial_id=data["trial_id"],
        participant_id=data["participant_id"],
        visit_date=data["visit_date"],
        blood_pressure=data["blood_pressure"],
        temperature=data["temperature"],
        notes=data["notes"]
    )

    db.add(obs)
    db.commit()

    return {"message": "Observation recorded"}

# ================= SUBMIT REPORT =================
@router.post("/report")
def submit_report(data: ReportCreate, db: Session = Depends(get_db)):

    report = Report(
        trial_id=data.trial_id,
        researcher_id=data.researcher_id,
        summary=data.summary,
        result=data.result,
        status="Pending"
    )

    db.add(report)
    db.commit()

    return {"message": "Report submitted"}



@router.post("/eligibility")
def create_criteria(data: dict, db: Session = Depends(get_db)):

    criteria = EligibilityCriteria(
        trial_id=data["trial_id"],
        min_age=data["min_age"],
        max_age=data["max_age"],
        required_condition=data["condition"],
        exclusions=data["exclusions"]
    )

    db.add(criteria)
    db.commit()

    return {"message": "Criteria added"}

# ================= HEALTH CHECK =================
@router.get("/")
def researcher_home():
    return {"message": "Researcher API active"}