from __future__ import annotations

import yaml
from pathlib import Path

from core.family_registry import FamilyRegistry, LensSpec


REGISTRY_PATH = Path("config/family_registry.yaml")


def load_family_registry() -> FamilyRegistry:
    registry = FamilyRegistry()
    if not REGISTRY_PATH.exists():
        return registry

    data = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8")) or []
    for entry in data:
        spec = LensSpec(
            id=entry["id"],
            display_name=entry["display_name"],
            lens=entry["lens"],
            role=entry["role"],
            status=entry["status"],
            scope=entry.get("scope", []),
            tool_surface=entry.get("tool_surface", []),
            invariants=entry.get("invariants", []),
            test_plan=entry["test_plan"],
            escalation=entry.get("escalation", []),
            created_at=entry["created_at"],
            updated_at=entry["updated_at"],
        )
        registry.register(spec)
    return registry


def dump_family_registry(registry: FamilyRegistry) -> None:
    entries = []
    for spec in registry.members.values():
        entries.append(
            {
                "id": spec.id,
                "display_name": spec.display_name,
                "lens": spec.lens,
                "role": spec.role,
                "status": spec.status,
                "scope": spec.scope,
                "tool_surface": spec.tool_surface,
                "invariants": spec.invariants,
                "test_plan": spec.test_plan,
                "escalation": spec.escalation,
                "created_at": spec.created_at,
                "updated_at": spec.updated_at,
                "hash": spec.hash,
            }
        )

    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(yaml.safe_dump(entries, sort_keys=False), encoding="utf-8")


if __name__ == "__main__":
    # Example: load and immediately rewrite to refresh hashes.
    reg = load_family_registry()
    dump_family_registry(reg)
