from hashlib import sha256
from typing import List
from app.models import Payload as CachedPayload
from app.repository.payload_repository import PayloadRepository

class PayloadService:
    def __init__(self, repository: PayloadRepository):
        self.repository = repository

    def transformer(self, input_str: str) -> str:
        return input_str.upper()

    def generate_cache_key(self, list_1: List[str], list_2: List[str]) -> str:
        combined = ",".join(list_1 + list_2)
        return sha256(combined.encode()).hexdigest()

    def interleave_payload(self, list_1: List[str], list_2: List[str]) -> str:
        transformed_list_1 = [self.transformer(item) for item in list_1]
        transformed_list_2 = [self.transformer(item) for item in list_2]
        interleaved = [item for pair in zip(transformed_list_1, transformed_list_2) for item in pair]
        return ", ".join(interleaved)

    def get_or_create_payload(self, list_1: List[str], list_2: List[str]) -> CachedPayload:
        cache_key = self.generate_cache_key(list_1, list_2)

        cached_payload = self.repository.get_payload_by_id(cache_key)
        if cached_payload:
            return cached_payload

        interleaved_payload = self.interleave_payload(list_1, list_2)
        new_payload = CachedPayload(id=cache_key, payload=interleaved_payload)

        self.repository.save_payload(new_payload)
        return new_payload
