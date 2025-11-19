from fastapi.testclient import TestClient
from src.core_bot_api.main import app
from fastapi import status

client = TestClient(app=app)


def test_home_page_return() -> None:
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Server started"}
