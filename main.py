import json
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import redis
from redis.commands.json.path import Path
from datetime import datetime

app = FastAPI(title="Exchange Rate API")
r = redis.Redis(host="redis", port=6379, db=0)


class Currency(BaseModel):
    name: str
    value: float


class DB(BaseModel):
    data: List[Currency]


db = DB(data=[])
data = json.load(open('all_currency.json', "r"))


@app.get("/")
def index():
    try:
        history = r.execute_command("GET", "counter1")
        return {"history": history}
    except:
        return {'key': 'value'}



@app.post('/currency')
def create_currency(currency: Currency):  # create currency object
    db.data.append(currency)
    return currency.dict()  # return last object from db list


@app.get('/currency/{currency_id}')
def get_currency_by_id(currency_id: str):
    r.incr('counter1')
    try:
        return data[currency_id]
    except:
        return {"error": "no data"}


@app.get('/currency/')
def get_all_currency():
    cache = rd.get(get_all_currency)
    return data


@app.delete('/currency/{currency_id}')
def delete_currency(currency_id: str):
    for index, key, in enumerate(db.data):
        for k, v in key:
            if k == "name" and v == currency_id:
                db.data.pop(index)
                return {"deleted": "successfully"}
    return {"error": "no data"}
