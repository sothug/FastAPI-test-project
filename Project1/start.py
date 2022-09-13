import uvicorn
import config

if __name__ == "__main__":
    uvicorn.run("app:app_p1", host=config.host, port=config.port, reload=config.reload)