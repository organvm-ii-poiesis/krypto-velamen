from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from ..models.analysis import ConnectorType
from ..models.report import DiagnosticIssue, DiagnosticSeverity

class DiagnosticType(str, Enum):
    CAUSAL_BINDING = "causal_binding"
    REORDERABILITY = "reorderability"
    NECESSITY = "necessity"
    INFORMATION_ECONOMY = "information_economy"
    FRAMEWORK = "framework"

class SceneTransition(BaseModel):
    from_scene: int
    to_scene: int
    connector: Optional[ConnectorType] = None
    explanation: Optional[str] = None
    is_causal: bool = False

class DiagnosticContext(BaseModel):
    title: str
    scenes: List[dict] = Field(default_factory=list)
    characters: List[str] = Field(default_factory=list)
    active_studies: List[str] = Field(default_factory=list)
    transitions: List[SceneTransition] = Field(default_factory=list)
    beat_map_available: bool = False

class DiagnosticThresholds(BaseModel):
    causal_binding_excellent: float = 0.80
    causal_binding_good: float = 0.60
    causal_binding_adequate: float = 0.30
    causal_binding_critical: float = 0.15
    reorderability_excellent: float = 0.05
    reorderability_good: float = 0.15
    reorderability_warning: float = 0.30
    reorderability_critical: float = 0.50
    necessity_excellent: float = 0.95
    necessity_good: float = 0.85
    necessity_warning: float = 0.70
    necessity_critical: float = 0.50
