from fastapi import FastAPI

app_p2 = FastAPI()

@app_p2.get("/")
def root():
    return {"data": "project2 message"}

@app_p2.get("/get_data")
def get_data():
    return {"data": "project2 content"}