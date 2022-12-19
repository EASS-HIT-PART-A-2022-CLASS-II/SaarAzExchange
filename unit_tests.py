from fastapi.testclient import TestClient
from pydantic import BaseModel

from main import app

client = TestClient(app)


class Data(BaseModel):
    name: str
    value: float


data = Data(name="$", value=3.58)


def test_create_currency():
    response = client.post('/currency', json=data.dict())
    assert response.status_code == 200
    assert response.json() == data


def test_get_all_currency():
    # response = client.post('/currency', json=data)
    # assert response.status_code == 200
    global data
    response = client.get('/currency/')
    assert response.status_code == 200
    assert data in response.json()["data"]


def test_get_currency_by_id():
    response = client.get('/currency/$')
    assert response.status_code == 200
    assert response.json() == data


def test_delete_currency():
    response = client.delete('/currency/$')
    assert response.status_code == 200
    assert response.json() == {"deleted": "successfully"}

