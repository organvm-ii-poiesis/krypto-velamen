from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from .models import DiagnosticContext, DiagnosticThresholds, DiagnosticType
from ..models.report import DiagnosticIssue, DiagnosticSeverity

class BaseDiagnostic(ABC):
    diagnostic_type: DiagnosticType
    description: str = ""

    def __init__(self, thresholds: Optional[DiagnosticThresholds] = None):
        self.thresholds = thresholds or DiagnosticThresholds()

    @abstractmethod
    def run(self, context: DiagnosticContext) -> List[DiagnosticIssue]:
        pass

    @abstractmethod
    def calculate_score(self, context: DiagnosticContext) -> float:
        pass

    def create_issue(
        self,
        description: str,
        severity: DiagnosticSeverity,
        location: Optional[str] = None,
        recommendation: str = "",
        category: str = "structure",
    ) -> DiagnosticIssue:
        issue_id = f"{self.diagnostic_type.value[:2].upper()}-{hash(description) % 1000:03d}"
        return DiagnosticIssue(
            id=issue_id,
            severity=severity,
            category=category,
            description=description,
            location=location,
            recommendation=recommendation,
            framework_source=self.diagnostic_type.value,
        )
