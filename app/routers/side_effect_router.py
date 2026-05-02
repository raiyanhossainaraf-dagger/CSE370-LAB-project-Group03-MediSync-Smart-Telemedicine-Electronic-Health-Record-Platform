from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.side_effect_model import SideEffect
from app.models.trial_model import Trial

router = APIRouter(prefix="/side-effect", tags=["Side Effect"])


@router.post("/report")
def report_side_effect(data: dict, db: Session = Depends(get_db)):

    new_effect = SideEffect(
        trial_id=data.get("trial_id", 1),  # optional fallback
        participant_id=data["participant_id"],  # ✅ NOW STORED
        effect_type=data["effect_type"],
        severity=data["severity"],
        duration=data["duration"]
    )

    db.add(new_effect)
    db.commit()

    return {"message": "Side effect reported successfully"}

@router.get("/participant/{participant_id}")
def get_participant_effects(participant_id: int, db: Session = Depends(get_db)):

    results = (
        db.query(
            SideEffect.effect_type,
            SideEffect.severity,
            SideEffect.duration,
            Trial.trial_name
        )
        .join(Trial, Trial.trial_id == SideEffect.trial_id)
        .filter(SideEffect.participant_id == participant_id)
        .all()
    )

    return [
        {
            "trial": r[3],
            "effect": r[0],
            "severity": r[1],
            "duration": r[2]
        }
        for r in results
    ]