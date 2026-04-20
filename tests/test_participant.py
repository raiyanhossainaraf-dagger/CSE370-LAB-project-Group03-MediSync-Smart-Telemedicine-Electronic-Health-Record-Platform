# tests/test_participant.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_participants():
    response = client.get("/participants/")

    assert response.status_code == 200