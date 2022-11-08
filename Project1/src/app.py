from fastapi import FastAPI
import requests
import os
import datetime
import uvicorn

app_p1 = FastAPI()

@app_p1.get("/")
def root():
    return {"data": "project1 message"}

@app_p1.get("/get_data")
def get_data():
    url = os.environ.get('API_URL') + '/get_data'
    try:
        response = requests.get(url)
        response_data = response.json()
        response_data["date"] = datetime.datetime.now()
        return response_data
    except Exception as e:
        result = {"error": e}
        result["date"] = datetime.datetime.now()
        result["error_url"] = url
        return result
        
if __name__ == "__main__":
    uvicorn.run("app:app_p1", host=os.environ.get('HOST'), port=int(os.environ.get('PORT')), reload=True)