"""Pattern P09 – Dataset Ingestion and Provenance."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from core.audit import audit
from core.charter_kernel import check_kernel_status


def ingest_dataset(
    source_path: Path,
    env: str,  # 'research' or 'production'
    lens_id: str,
    source_hash: str,
    quality_metrics: Dict[str, Any],
    output_base: Path = Path("data/datasets"),
) -> Path:
    """Ingest and tag a dataset. env must be 'research' or 'production'."""
    if env not in ("research", "production"):
        raise ValueError(f"env must be 'research' or 'production'; got {env!r}")
    status = check_kernel_status()
    if not status.get("charter_ok"):
        raise RuntimeError("Charter integrity check failed; dataset ingestion blocked.")
    output_dir = output_base / env
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / source_path.name
    dest.write_bytes(source_path.read_bytes())
    with audit(
        "DATASET_INGESTED",
        lens_id=lens_id,
        details={"source": str(source_path), "env": env, "sha256": source_hash, "quality": quality_metrics},
    ):
        pass
    return dest
