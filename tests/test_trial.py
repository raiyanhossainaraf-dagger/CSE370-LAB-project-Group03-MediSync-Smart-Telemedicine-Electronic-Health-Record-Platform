# tests/test_trial.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_trials():
    response = client.get("/trials/")

    assert response.status_code == 200


def test_create_trial():
    response = client.post("/trials/", json={
        "trial_name": "Cancer Trial",
        "drug_name": "MedX",
        "phase": "Phase II",
        "start_date": "2026-05-01",
        "end_date": "2026-09-01",
        "duration": 120,
        "researcher_id": 1,
        "admin_id": 1
    })

    assert response.status_code == 200