from fastapi import FastAPI

app_p2 = FastAPI()

@app_p2.get("/")
def root(message: str):
    return {"data": message}

@app_p2.get("/get_data")
def get_data():
    return {"data": "content"}