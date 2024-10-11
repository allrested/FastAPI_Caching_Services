from fastapi import Depends
from sqlmodel import Session
from app.database import get_session
from app.repository.payload_repository import PayloadRepository
from app.services.payload_service import PayloadService

def get_payload_service(session: Session = Depends(get_session)):
    repository = PayloadRepository(session)
    return PayloadService(repository)
