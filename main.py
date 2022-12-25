from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Exchange Rate API")


class Currency(BaseModel):
    name: str
    value: float


class DB(BaseModel):
    data: List[Currency]


db = DB(data=[])


@app.get("/")
def index():
    return {'key': 'value'}


@app.post('/currency')
def create_currency(currency: Currency):  # create currency object
    db.data.append(currency)
    return currency.dict()  # return last object from db list


@app.get('/currency/{currency_id}')
def get_currency_by_id(currency_id: str):
    for key in db.data:
        for k, v in key:
            if k == "name" and v == currency_id:
                return key.dict()
    return {"error": "no data"}


@app.get('/currency/')
def get_all_currency():
    return db.dict()


@app.delete('/currency/{currency_id}')
def delete_currency(currency_id: str):
    for index, key, in enumerate(db.data):
        for k, v in key:
            if k == "name" and v == currency_id:
                db.data.pop(index)
                return {"deleted": "successfully"}
    return {"error": "no data"}

