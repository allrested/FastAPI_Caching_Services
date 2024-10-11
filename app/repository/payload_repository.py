from sqlmodel import Session, select
from app.models import Payload


class PayloadRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_payload_by_id(self, payload_id: str) -> Payload:
        """Fetch cached payload by ID from the database"""
        return self.session.exec(
            select(Payload).where(Payload.id == payload_id)
        ).first()

    def save_payload(self, payload: Payload) -> None:
        """Store a new cached payload in the database"""
        self.session.add(payload)
        self.session.commit()
