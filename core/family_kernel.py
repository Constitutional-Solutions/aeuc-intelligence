"""AEUC Family Kernel.

This module ties together core boot-time checks for the AEUC family:

- Charter integrity (via core.charter_kernel).
- Sabbath status.
- Family registry availability.

Higher-level orchestration should build on top of these primitives.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from core.charter_kernel import verify_charter
from core.sabbath import is_sabbath
from scripts.build_family_registry import load_family_registry


@dataclass
class KernelStatus:
    charter_ok: bool
    is_sabbath_now: bool
    active_member_ids: list[str]


def check_kernel_status(repo_root: Path | None = None) -> KernelStatus:
    if repo_root is None:
        repo_root = Path(__file__).resolve().parents[1]

    charter_path = repo_root / "docs" / "FAMILY_CHARTER.md"
    charter_ok = charter_path.exists() and verify_charter(charter_path)

    now = datetime.now(timezone.utc)
    sabbath_now = is_sabbath(now)

    registry = load_family_registry()
    active_ids = [spec.id for spec in registry.members.values() if spec.status == "active"]

    return KernelStatus(
        charter_ok=charter_ok,
        is_sabbath_now=sabbath_now,
        active_member_ids=active_ids,
    )
