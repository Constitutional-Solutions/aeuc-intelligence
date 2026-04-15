"""Pattern P05 – Change Proposal and Hazard Assessment.

This module is the production implementation of CH15_P05_CHANGE_PROPOSAL.md.
All functions emit AuditEvents via core.audit and verify Charter integrity
before high-risk operations.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from core.audit import AuditEvent, audit
from core.charter_kernel import check_kernel_status
from core.time_utils import now_utc


@dataclass
class Hazard:
    category: str
    description: str
    severity: int   # 1-5
    likelihood: int  # 1-5

    @property
    def score(self) -> int:
        return self.severity * self.likelihood

    @property
    def tier(self) -> int:
        if self.score <= 4:
            return 1
        if self.score <= 12:
            return 2
        return 3


@dataclass
class ChangeRecord:
    change_id: str
    proposer_id: str
    affected_systems: List[str]
    description: str
    evidence_references: List[str]
    proposed_at: datetime = field(default_factory=now_utc)
    hazards: List[Hazard] = field(default_factory=list)
    max_tier: int = 1
    status: str = "proposed"  # proposed | approved | rejected | deployed | rolled_back


def propose_change(
    change_id: str,
    proposer_id: str,
    affected_systems: List[str],
    description: str,
    evidence_references: List[str],
    output_dir: Path = Path("data/changes/proposed"),
) -> ChangeRecord:
    """Open a new Change Record after verifying Charter integrity."""
    status = check_kernel_status()
    if not status.get("charter_ok"):
        raise RuntimeError("Charter integrity check failed; change proposal quarantined.")

    record = ChangeRecord(
        change_id=change_id,
        proposer_id=proposer_id,
        affected_systems=affected_systems,
        description=description,
        evidence_references=evidence_references,
    )
    with audit("CHANGE_PROPOSED", lens_id=proposer_id, details={"change_id": change_id}):
        output_dir.mkdir(parents=True, exist_ok=True)
        # Persist as YAML or JSON in production; stub here.
    return record
