from fastapi import Depends
from sqlmodel import Session
from database import get_session
from repository.payload_repository import PayloadRepository
from services.payload_service import PayloadService

def get_payload_service(session: Session = Depends(get_session)):
    repository = PayloadRepository(session)
    return PayloadService(repository)
