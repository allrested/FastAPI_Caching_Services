from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api import payloads
from app.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs when the application starts
    create_db_and_tables()


app = FastAPI()

# Include the payload routes
app.include_router(payloads.router)
