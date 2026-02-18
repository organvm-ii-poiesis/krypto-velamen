from .base import BaseDiagnostic
from .models import DiagnosticContext, DiagnosticType, SceneTransition
from ..models.analysis import ConnectorType
from ..models.report import DiagnosticIssue, DiagnosticSeverity

class CausalBindingDiagnostic(BaseDiagnostic):
    diagnostic_type = DiagnosticType.CAUSAL_BINDING
    description = "Analyzes causal binding between scenes"

    def run(self, context: DiagnosticContext) -> List[DiagnosticIssue]:
        issues = []
        score = self.calculate_score(context)
        
        overall_severity = DiagnosticSeverity.INFO
        if score < 0.30: overall_severity = DiagnosticSeverity.CRITICAL
        elif score < 0.60: overall_severity = DiagnosticSeverity.WARNING
        
        issues.append(self.create_issue(
            description=f"Overall causal binding ratio: {score:.0%}",
            severity=overall_severity,
            recommendation="Target > 60% causal connectors (BUT/THEREFORE)"
        ))
        
        return issues

    def calculate_score(self, context: DiagnosticContext) -> float:
        if not context.scenes: return 0.0
        
        causal_count = 0
        total_eval = 0
        
        for i in range(len(context.scenes) - 1):
            scene = context.scenes[i]
            connector = scene.get("connector")
            if connector:
                total_eval += 1
                if connector.upper() in ["BUT", "THEREFORE"]:
                    causal_count += 1
        
        return causal_count / total_eval if total_eval > 0 else 0.0
