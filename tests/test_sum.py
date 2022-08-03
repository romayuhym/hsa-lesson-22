from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_success_ints():
    response = client.get("/sum/1/2")
    assert response.status_code == 200
    assert response.json() == {"sum": 3}


def test_success_floats():
    response = client.get("/sum/1/2.2")
    assert response.status_code == 200
    assert response.json() == {"sum": 3.2}


def test_success_not_a_number():
    response = client.get("/sum/1/a")
    assert response.status_code == 200
    assert "error" in response.json().keys()
