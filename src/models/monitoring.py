"""Pattern P12 – Model Monitoring and Drift Response."""
from __future__ import annotations

from core.audit import audit


def record_monitoring_run(model_id: str, metrics: dict, lens_id: str = "TRUTH-Q") -> None:
    with audit("MONITORING_RUN", lens_id=lens_id, details={"model_id": model_id, "metrics": metrics}):
        pass


def flag_drift(model_id: str, severity: str, details: dict, lens_id: str = "RISK-Q") -> None:
    """severity: 'low' | 'medium' | 'high'"""
    with audit("DRIFT_DETECTED", lens_id=lens_id, details={"model_id": model_id, "severity": severity, **details}):
        pass


def suspend_model(model_id: str, reason: str, lens_id: str) -> None:
    with audit("MODEL_SUSPENDED", lens_id=lens_id, details={"model_id": model_id, "reason": reason}):
        pass
