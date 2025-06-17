from sqlmodel import Session, create_engine

engine = create_engine("sqlite:///./app_data.db", echo=True)


def get_session():
    """Create a new SQLModel session."""
    session = Session(engine)
    yield session
