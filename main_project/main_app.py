from fastapi import FastAPI, Request
from sub_project import sub_app
import requests

main_app = FastAPI()
main_app.mount('/sub_app', sub_app.sub_app)

@main_app.get("/")
def root(request: Request):
    host = request.client.host
    port = 8000 # request.client.port
    url = fr"http://{host}:{port}/sub_app/"
    response = requests.get(url)
    return response.json()