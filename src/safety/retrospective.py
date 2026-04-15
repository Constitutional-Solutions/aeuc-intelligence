"""Pattern P08 – Post-Change Retrospective."""
from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone

from core.audit import audit
from core.time_utils import now_utc


def write_retrospective(
    change_id: str,
    narrative: str,
    lens_id: str = "EVAL-Q",
    stories_dir: Path = Path("archive/stories"),
) -> Path:
    """Write a narrative retrospective file and emit RETROSPECTIVE_COMPLETE."""
    stories_dir.mkdir(parents=True, exist_ok=True)
    date_str = now_utc().strftime("%Y-%m-%d")
    out_path = stories_dir / f"{date_str}-change-{change_id}.md"
    out_path.write_text(f"# Retrospective: Change {change_id}\n\n{narrative}\n", encoding="utf-8")
    with audit("RETROSPECTIVE_COMPLETE", lens_id=lens_id, details={"change_id": change_id, "file": str(out_path)}):
        pass
    return out_path
