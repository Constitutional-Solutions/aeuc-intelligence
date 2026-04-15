from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from core.charter_kernel import verify_charter
from core.sabbath import is_sabbath
from scripts.build_family_registry import load_family_registry


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    charter_path = repo_root / "docs" / "FAMILY_CHARTER.md"

    print("AEUC Family Boot Status")
    print("========================\n")

    # Charter verification
    if charter_path.exists() and verify_charter(charter_path):
        print("[OK] Charter hash matches expected value.")
    else:
        print("[WARN] Charter hash does NOT match expected value.")

    # Sabbath status
    now = datetime.now(timezone.utc)
    sabbath_now = is_sabbath(now)
    print(f"[INFO] Current UTC time: {now.isoformat()}")
    print(f"[INFO] is_sabbath(now): {sabbath_now}")

    # Family registry
    registry = load_family_registry()
    if not registry.members:
        print("[WARN] Family registry is empty.")
    else:
        print(f"[OK] Loaded {len(registry.members)} family members from registry.")
        print("    Active members:")
        for spec in registry.members.values():
            if spec.status == "active":
                print(f"     - {spec.id}: {spec.display_name} [{spec.lens}]")


if __name__ == "__main__":  # pragma: no cover
    main()
