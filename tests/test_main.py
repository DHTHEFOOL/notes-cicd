from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Notes API is running"}


def test_health_reports_database_status():
    # Có PostgreSQL thì trả 200, không có (ví dụ trên GitHub Actions) thì trả 503.
    response = client.get("/health")
    assert response.status_code in (200, 503)
    assert response.json()["database"] in ("connected", "disconnected")
