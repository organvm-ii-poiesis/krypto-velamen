from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from narratological.diagnostics.causal import CausalBindingDiagnostic
from narratological.diagnostics.models import DiagnosticContext
from narratological.models.report import AnalysisReport, DiagnosticIssue
import datetime

app = FastAPI(title="KRYPTO-VELAMEN Lens Engine")

class AnalysisRequest(BaseModel):
    title: str
    scenes: List[dict]

@app.get("/")
def root():
    return {"status": "active", "service": "lens-engine", "framework": "Narratological Lenses"}

@app.post("/diagnose/causal", response_model=AnalysisReport)
def diagnose_causal(req: AnalysisRequest):
    context = DiagnosticContext(
        title=req.title,
        scenes=req.scenes
    )
    
    diagnostic = CausalBindingDiagnostic()
    issues = diagnostic.run(context)
    score = diagnostic.calculate_score(context)
    
    return AnalysisReport(
        title=f"Causal Analysis: {req.title}",
        script_id="unknown",
        created_at=datetime.datetime.now().isoformat(),
        issues=issues,
        metrics={"causal_binding_ratio": score},
        summary=f"Analysis complete. Score: {score:.2f}"
    )
