"""Pattern P11 – Model Evaluation and Promotion Gate."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from core.audit import audit
from core.charter_kernel import check_kernel_status


def request_promotion(model_id: str, experiment_id: str, lens_id: str) -> None:
    status = check_kernel_status()
    if not status.get("charter_ok"):
        raise RuntimeError("Charter integrity check failed; promotion request blocked.")
    with audit("PROMOTION_REQUESTED", lens_id=lens_id, details={"model_id": model_id, "experiment_id": experiment_id}):
        pass


def promote_model(model_id: str, lens_id: str, production_dir: Path = Path("data/models/production")) -> None:
    production_dir.mkdir(parents=True, exist_ok=True)
    with audit("MODEL_PROMOTED", lens_id=lens_id, details={"model_id": model_id}):
        pass


def reject_model(model_id: str, reason: str, lens_id: str) -> None:
    with audit("MODEL_REJECTED", lens_id=lens_id, details={"model_id": model_id, "reason": reason}):
        pass
