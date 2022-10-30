from fastapi import FastAPI
import requests
import config
from datetime import datetime

app_p1 = FastAPI()

@app_p1.get("/")
def root():
    return {"data": "root"}

@app_p1.get("/get_data/")
def get_data():
    try:
        url = fr"http://{config.another_host}:{config.another_port}/get_data"
        response = requests.get(url)
        result = response.json()
        result["datetime"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        ...
        return result
    except Exception as e:
        return {"error": e}