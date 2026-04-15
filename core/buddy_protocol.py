from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class BuddyPair:
    primary_id: str
    buddy_id: str


class BuddyRegistry:
    """In-memory mapping of buddy relationships between lenses.

    In a full deployment this can be persisted alongside the FamilyRegistry.
    """

    def __init__(self) -> None:
        self._buddies: Dict[str, List[str]] = {}

    def assign_buddy(self, primary_id: str, buddy_id: str) -> None:
        self._buddies.setdefault(primary_id, [])
        if buddy_id not in self._buddies[primary_id]:
            self._buddies[primary_id].append(buddy_id)

    def buddies_for(self, primary_id: str) -> List[str]:
        return list(self._buddies.get(primary_id, []))
