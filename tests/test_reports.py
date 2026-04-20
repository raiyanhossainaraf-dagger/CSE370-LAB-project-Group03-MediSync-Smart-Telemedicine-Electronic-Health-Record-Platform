# tests/test_reports.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_report_summary():
    response = client.get("/reports/summary")

    assert response.status_code == 200