from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_random_profiles():
    response = client.get("/profiles/random")
    print(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    # Further assertions can be made if you mock the database or use test data
