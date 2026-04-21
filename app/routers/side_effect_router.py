from fastapi import APIRouter

router = APIRouter(prefix="/side-effects", tags=["Side Effects"])

@router.get("/")
def get_side_effects():
    return {"message": "All side effects"}