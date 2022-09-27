import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings, Settings
from .customer_api import router as customer_router

app = FastAPI()
app.include_router(customer_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("uvicorn")


@app.get("/")
def index() -> dict:
    return {"Hello": "World"}


@app.on_event("startup")
def startup_event() -> None:
    settings: Settings = get_settings()
    logging.info(f"Starting app in {settings.environment} environment")


@app.on_event("shutdown")
def shutdown_event() -> None:
    logging.info("Stopping app")


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="debug"
    )
