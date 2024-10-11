from sqlmodel import Session, select
from models import CachedPayload

class PayloadRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_payload_by_id(self, payload_id: str) -> CachedPayload:
        """Fetch cached payload by ID from the database"""
        return self.session.exec(select(CachedPayload).where(CachedPayload.id == payload_id)).first()

    def save_payload(self, payload: CachedPayload) -> None:
        """Store a new cached payload in the database"""
        self.session.add(payload)
        self.session.commit()
