"""API tests for the health-check service."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_ok_returns_expected_status() -> None:
    """GET /ok returns the specified successful health response."""
    response = client.get("/ok")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version_returns_expected_response() -> None:
    """GET /version returns the current service version."""
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}
