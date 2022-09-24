import fastapi
import uvicorn

from app import customer_api

app = fastapi.FastAPI()
app.include_router(customer_api.router)


@app.get("/")
def index() -> dict:
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="debug"
    )
