from fastapi import FastAPI

from .api.endpoints.prediction_requests import prediction_requests_router

app = FastAPI()

app.include_router(
    prediction_requests_router, prefix="/api", tags=["prediction_requests"]
)
