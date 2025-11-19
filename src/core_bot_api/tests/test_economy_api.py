from fastapi.testclient import TestClient
from src.core_bot_api.main import app
from fastapi import status

client = TestClient(app=app)


async def test_russian_roulette_succes_status_code():
    response = client.get("/economy/russian_roulette/100")
    assert response.status_code == status.HTTP_200_OK
