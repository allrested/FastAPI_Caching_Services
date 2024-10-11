from sqlmodel import SQLModel, Field


class Payload(SQLModel, table=True):
    id: str = Field(primary_key=True)
    payload: str
