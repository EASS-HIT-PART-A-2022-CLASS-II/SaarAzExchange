import json

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

data = {
    "name": "$",
    "value": 3.58
}


def test_create_currency():
    response = client.post('/currency', json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_get_all_currency():
    response = client.get('/currency/')
    print(response.json())
    assert response.status_code == 200
    assert data in response.json()


def test_get_currency_by_id():
    response = client.get('/currency/{currency_id}', json=data)
    assert response.status_code == 200
    assert response.json() == data
    print(response.json())


def test_delete_currency():
    response = client.delete('/currency/{currency_id}')
    assert response.status_code == 200
    assert response.json() == {
        "name": "Test",
        "value": 1
    }
