from fastapi import FastAPI
import requests
import config

app_p1 = FastAPI()

@app_p1.get("/")
def root(message: str=""):
    return {"data": "project1 message"}

@app_p1.get("/another_api/{api_request}")
def get_data(api_request: str|None):
    #print(api_request)
    url = fr"http://{config.another_host}:{config.another_port}/{api_request}"
    response = requests.get(url)
    response_data = response.json()
    response_data["from"] = f"{config.another_host}:{config.another_port}"
    return response_data