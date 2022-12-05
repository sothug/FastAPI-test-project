from fastapi import FastAPI
import uvicorn

app_p2 = FastAPI(openapi_url=f"/api/v1/project2/openapi.json", docs_url="/api/v1/project2/docs")

@app_p2.get("/api/v1/project2/")
def root():
    return {"data": "project2 message"}

@app_p2.get("/api/v1/project2/get_data")
def get_data():
    return {"data": "project2 content"}

if __name__ == "__main__":
    uvicorn.run("app:app_p2", host='0.0.0.0', port=80, reload=True)