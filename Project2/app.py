from fastapi import FastAPI

app_p2 = FastAPI()

@app_p2.get("/")
def root():
    return {"data": "root"}

@app_p2.get("/get_data/")
def get_data():
    return {"data": "content"}

@app_p2.get("/get_data/{id}")
def get_data(id: int):
    return {"data": "content", "id": id}