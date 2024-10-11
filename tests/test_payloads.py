import pytest
from fastapi.testclient import TestClient
from app.main import app  # Correct absolute import
from app.database import create_db_and_tables

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_db():
    create_db_and_tables()


def test_create_payload():
    payload = {
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"],
    }
    response = client.post("/payload", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["message"] == "Payload generated"


def test_get_payload():
    payload = {
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"],
    }
    post_response = client.post("/payload", json=payload)
    payload_id = post_response.json()["id"]

    get_response = client.get(f"/payload/{payload_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert (
        data["output"]
        == "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"
    )


def test_get_payload_not_found():
    response = client.get("/payload/99999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Payload not found"
