from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os
from pathlib import Path

app = FastAPI(title="KRYPTO-VELAMEN Archive API")

# Path to the legacy orchestrator
ORCHESTRATOR_PATH = Path("tools/orchestrator.py")

class ScaffoldRequest(BaseModel):
    slug: str
    preset: str = "confessional-whisper"
    visibility: bool = False

@app.get("/")
def root():
    return {"service": "archive-engine", "status": "legacy-connected"}

@app.get("/dashboard")
def get_dashboard():
    # Execute the legacy orchestrator and capture output
    result = subprocess.run(
        ["python3", str(ORCHESTRATOR_PATH), "dashboard"],
        capture_output=True, text=True
    )
    return {"raw_output": result.stdout}

@app.post("/scaffold")
def scaffold_fragment(req: ScaffoldRequest):
    cmd = ["python3", str(ORCHESTRATOR_PATH), "scaffold", "--slug", req.slug, "--preset", req.preset]
    if req.visibility:
        cmd.append("--visibility")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=result.stderr)
    
    return {"message": "Fragment scaffolded successfully", "output": result.stdout}
