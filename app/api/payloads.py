from fastapi import APIRouter, Depends, HTTPException
from app.schemas import PayloadRequest
from app.services.payload_service import PayloadService
from app.dependencies import get_payload_service

router = APIRouter()

@router.post("/payload")
def create_payload(payload: PayloadRequest, service: PayloadService = Depends(get_payload_service)):
    cached_payload = service.get_or_create_payload(payload.list_1, payload.list_2)
    return {"message": "Payload generated", "id": cached_payload.id}

@router.get("/payload/{id}")
def get_payload(id: str, service: PayloadService = Depends(get_payload_service)):
    cached_payload = service.repository.get_payload_by_id(id)
    if not cached_payload:
        raise HTTPException(status_code=404, detail="Payload not found")
    return {"output": cached_payload.payload}
