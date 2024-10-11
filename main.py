from fastapi import FastAPI
from api.payloads import router
from database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include the payload routes
app.include_router(router)
