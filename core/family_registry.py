from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Literal
import hashlib
import json

Status = Literal["active", "dormant", "quarantined", "candidate"]


@dataclass
class LensSpec:
    """Specification for a single family member (lens).

    This mirrors the YAML/JSON representation stored in family_registry.yaml.
    The hash field is computed from the other fields to support integrity checks.
    """

    id: str
    display_name: str
    lens: str
    role: str
    status: Status
    scope: List[str]
    tool_surface: List[str]
    invariants: List[str]
    test_plan: str
    escalation: List[str]
    created_at: str
    updated_at: str
    hash: str = field(init=False)

    def __post_init__(self) -> None:
        payload = {
            "id": self.id,
            "display_name": self.display_name,
            "lens": self.lens,
            "role": self.role,
            "status": self.status,
            "scope": self.scope,
            "tool_surface": self.tool_surface,
            "invariants": self.invariants,
            "test_plan": self.test_plan,
            "escalation": self.escalation,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        h = hashlib.blake2b(
            json.dumps(payload, sort_keys=True).encode("utf-8"), digest_size=32
        )
        object.__setattr__(self, "hash", h.hexdigest())


class FamilyRegistry:
    """In-memory registry of all family members.

    In a production deployment this registry should be loaded from and
    persisted to a signed YAML/JSON file (e.g. family_registry.yaml), and
    mutations should be wrapped in audit logging.
    """

    def __init__(self) -> None:
        self.members: Dict[str, LensSpec] = {}

    def register(self, spec: LensSpec) -> None:
        if spec.id in self.members:
            raise ValueError(f"Member {spec.id} already registered")
        self.members[spec.id] = spec

    def get(self, member_id: str) -> LensSpec:
        return self.members[member_id]

    def active_members(self) -> List[LensSpec]:
        return [m for m in self.members.values() if m.status == "active"]


def admit_member(registry: FamilyRegistry, candidate: LensSpec, votes: Dict[str, bool]) -> None:
    """Promote a candidate member to active status after unanimous consent.

    - All currently active members must have a vote recorded in `votes`.
    - All votes must be True for admission to succeed.
    """

    # Ensure candidate is not already active
    if candidate.id in registry.members and registry.get(candidate.id).status == "active":
        raise ValueError(f"{candidate.id} already active")

    # Check unanimous consent from existing active members
    active_ids = [m.id for m in registry.active_members()]
    missing_votes = set(active_ids) - set(votes.keys())
    if missing_votes:
        raise ValueError(f"Missing votes from: {', '.join(sorted(missing_votes))}")

    if not all(votes[m_id] for m_id in active_ids):
        raise ValueError("Unanimous consent not reached")

    # Promote candidate to active
    candidate.status = "active"
    candidate.updated_at = datetime.utcnow().isoformat()
    registry.register(candidate)
