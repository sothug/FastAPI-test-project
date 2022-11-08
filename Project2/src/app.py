from fastapi import FastAPI
import os
import uvicorn

app_p2 = FastAPI()

@app_p2.get("/")
def root():
    return {"data": "project2 message"}

@app_p2.get("/get_data")
def get_data():
    return {"data": "project2 content"}

if __name__ == "__main__":
    uvicorn.run("app:app_p2", host=os.environ.get('HOST'), port=int(os.environ.get('PORT')), reload=True)