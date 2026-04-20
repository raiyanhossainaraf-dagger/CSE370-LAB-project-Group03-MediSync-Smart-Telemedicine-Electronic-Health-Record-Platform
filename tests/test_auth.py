# tests/test_auth.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_admin():
    response = client.post("/auth/login", json={
        "username": "admin",
        "password": "1234"
    })

    assert response.status_code == 200
    assert response.json()["role"] == "Admin"


def test_logout():
    response = client.post("/auth/logout")

    assert response.status_code == 200