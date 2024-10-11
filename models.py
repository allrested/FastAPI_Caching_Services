from sqlmodel import SQLModel, Field

class CachedPayload(SQLModel, table=True):
    id: str = Field(primary_key=True)
    payload: str
