"""Pattern P07 – Controlled Deployment and Rollback."""
from __future__ import annotations

from core.audit import audit
from core.charter_kernel import check_kernel_status
from core.sabbath import is_sabbath
from core.time_utils import now_utc


def pre_deployment_checks(change_id: str, lens_id: str = "HUMAN-DIRECTOR") -> None:
    """Run pre-deployment checklist; raise if any check fails."""
    status = check_kernel_status()
    if not status.get("charter_ok"):
        raise RuntimeError(f"Charter integrity failed; deployment of {change_id} blocked.")
    if is_sabbath(now_utc()):
        raise RuntimeError(
            f"Sabbath is active; deployment of {change_id} requires HUMAN-DIRECTOR emergency declaration."
        )


def record_deployment_step(change_id: str, step: str, lens_id: str) -> None:
    with audit("DEPLOYMENT_STEP", lens_id=lens_id, details={"change_id": change_id, "step": step}):
        pass


def execute_rollback(change_id: str, reason: str, lens_id: str) -> None:
    with audit("ROLLBACK_EXECUTED", lens_id=lens_id, details={"change_id": change_id, "reason": reason}):
        pass
