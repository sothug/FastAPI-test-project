from fastapi import FastAPI

sub_app = FastAPI()

@sub_app.get("/")
async def get_data():
    return {"data": "content"}