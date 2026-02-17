from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="KRYPTO-VELAMEN Identity Service")

class Profile(BaseModel):
    handle: str
    surveillance_level: int = 1
    is_public: bool = False

@app.get("/")
async def root():
    return {"status": "online", "service": "identity-service"}

@app.get("/profile/{handle}")
async def get_profile(handle: str):
    # This will eventually connect to PostgreSQL
    return {
        "handle": handle,
        "mask": "defensive-wit",
        "signal": "overdetermined-detail"
    }
