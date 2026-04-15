"""Pattern P06 – Review-Tiered Approval.

Routes a ChangeRecord to the correct review tier and collects votes.
"""
from __future__ import annotations

from typing import Dict, List

from core.audit import audit


TIER_REQUIRED_APPROVALS: Dict[int, List[str]] = {
    1: ["TRUTH-Q", "SAFE-Q"],
    2: ["TRUTH-Q", "SAFE-Q", "AUDIT-Q", "HUMAN-DIRECTOR"],
    3: [],  # Full family: resolved dynamically from registry
}


def collect_vote(
    change_id: str,
    lens_id: str,
    approved: bool,
    reason: str = "",
) -> None:
    """Record a single lens vote for a change at any tier."""
    event_type = "TIER_APPROVED" if approved else "TIER_OBJECTED"
    with audit(event_type, lens_id=lens_id, details={"change_id": change_id, "reason": reason}):
        pass


def is_approved(change_id: str, tier: int, votes: Dict[str, bool]) -> bool:
    """Return True if the required approvers for the tier have all voted True."""
    required = TIER_REQUIRED_APPROVALS.get(tier, [])
    if tier == 3:
        # Full family: all voters must approve
        return all(votes.values()) and len(votes) > 0
    return all(votes.get(lens_id, False) for lens_id in required)
