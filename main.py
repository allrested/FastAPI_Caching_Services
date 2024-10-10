from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Session, create_engine, select
from typing import List
import hashlib
import os

app = FastAPI()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./cache.db")
engine = create_engine(DATABASE_URL)


# Define SQLModel for storing cached payloads
class CachedPayload(SQLModel, table=True):
    id: str = Field(primary_key=True)
    payload: str


# Create the database table
SQLModel.metadata.create_all(engine)


# Pydantic model for incoming requests
class PayloadRequest(BaseModel):
    list_1: List[str]
    list_2: List[str]


# Simulated transformer function (external service simulation)
def transformer(input_str: str) -> str:
    return input_str.upper()


# Helper function to generate the cache key (identifier)
def generate_cache_key(list_1: List[str], list_2: List[str]) -> str:
    combined = ",".join(list_1 + list_2)
    return hashlib.sha256(combined.encode()).hexdigest()


# Helper function to create the interleaved payload
def interleave_payload(list_1: List[str], list_2: List[str]) -> str:
    transformed_list_1 = [transformer(item) for item in list_1]
    transformed_list_2 = [transformer(item) for item in list_2]
    interleaved = [item for pair in zip(transformed_list_1, transformed_list_2) for item in pair]
    return ", ".join(interleaved)


# Endpoint to create payload
@app.post("/payload")
def create_payload(payload: PayloadRequest):
    # Generate a unique identifier for this payload
    cache_key = generate_cache_key(payload.list_1, payload.list_2)

    # Check if the result is already cached
    with Session(engine) as session:
        cached_result = session.exec(select(CachedPayload).where(CachedPayload.id == cache_key)).first()
        if cached_result:
            return {"message": "Payload already exists", "id": cache_key}

        # Otherwise, generate the payload
        interleaved_payload = interleave_payload(payload.list_1, payload.list_2)

        # Store the result in the database
        new_cache = CachedPayload(id=cache_key, payload=interleaved_payload)
        session.add(new_cache)
        session.commit()

        return {"message": "Payload created", "id": cache_key}


# Endpoint to read payload by id
@app.get("/payload/{id}")
def get_payload(id: str):
    with Session(engine) as session:
        cached_result = session.exec(select(CachedPayload).where(CachedPayload.id == id)).first()
        if cached_result:
            return {"output": cached_result.payload}

        raise HTTPException(status_code=404, detail="Payload not found")
