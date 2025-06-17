from sqlmodel import Session, select

from ..database.models import PredictionRequest
from .session import get_session


def get_all_prediction_requests(session: Session) -> list[PredictionRequest]:
    """Get all prediction requests from the database."""

    return list(session.exec(select(PredictionRequest)).all())


def create_prediction_request(
    request: PredictionRequest, session: Session
) -> PredictionRequest:
    """Create a new prediction request in the database."""

    session.add(request)
    session.commit()
    session.refresh(request)

    return request
