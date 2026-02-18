from enum import Enum
from typing import Optional, List, Any
from pydantic import BaseModel, Field

class DiagnosticSeverity(str, Enum):
    INFO = "INFO"
    SUGGESTION = "SUGGESTION"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

class DiagnosticIssue(BaseModel):
    id: str
    severity: DiagnosticSeverity
    category: str
    description: str
    location: Optional[str] = None
    recommendation: str = ""
    framework_source: Optional[str] = None

class AnalysisReport(BaseModel):
    title: str
    script_id: str
    created_at: str
    issues: List[DiagnosticIssue] = Field(default_factory=list)
    metrics: dict = Field(default_factory=dict)
    summary: str = ""
