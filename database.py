from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager
import os

# Get the database URL from environment variables, default to SQLite if not set
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./cache.db")

# Create a SQLModel database engine
engine = create_engine(DATABASE_URL, echo=True)

# Dependency for session management in FastAPI
def get_session():
    """Provide a transactional scope for a series of operations within a request."""
    with Session(engine) as session:
        yield session


# Optional: For non-FastAPI contexts where a session is needed
@contextmanager
def get_contextual_session():
    """Context manager for session usage outside FastAPI request/response lifecycle."""
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# Create all tables (this is useful for initializing the database in dev environment)
def create_db_and_tables():
    """Create the database and all required tables."""
    SQLModel.metadata.create_all(engine)
