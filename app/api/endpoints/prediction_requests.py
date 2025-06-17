from fastapi import APIRouter, Depends

from ...database.crud import (create_prediction_request,
                              get_all_prediction_requests)
from ...database.models import PredictionRequest
from ...database.session import Session, get_session

prediction_requests_router = APIRouter()


@prediction_requests_router.get("/prediction_requests")
def get_prediction_requests(session: Session = Depends(get_session)):
    """Get all prediction requests."""

    return get_all_prediction_requests(session)


@prediction_requests_router.post("/prediction_requests")
def create_prediction_request_endpoint(
    prediction_request: PredictionRequest, session: Session = Depends(get_session)
):
    """Create a new prediction request."""

    return create_prediction_request(prediction_request, session)
