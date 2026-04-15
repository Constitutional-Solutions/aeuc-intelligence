"""Shared utilities for the AEUC accounting and records domain (Pattern P01–P04)."""
from __future__ import annotations

import csv
import hashlib
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Canonical ledger schema
# ---------------------------------------------------------------------------

CANONICAL_COLUMNS = [
    "entry_id",          # Unique identifier for the transaction line
    "entry_date",        # ISO-8601 date (YYYY-MM-DD)
    "posting_date",      # ISO-8601 date when posted to the GL
    "account_code",      # Chart-of-accounts code (string)
    "account_name",      # Human-readable account name
    "debit_amount",      # Decimal; 0 if credit-only line
    "credit_amount",     # Decimal; 0 if debit-only line
    "currency",          # ISO-4217 currency code
    "reporting_amount",  # Amount converted to reporting currency
    "exchange_rate",     # Rate used for conversion (1.0 if same currency)
    "narrative",         # Free-text description
    "source_system",     # System that generated the entry
    "import_timestamp",  # UTC timestamp when this record was ingested
    "audit_event_id",    # AuditEvent ID of the ingestion run
]


# ---------------------------------------------------------------------------
# Provenance helpers
# ---------------------------------------------------------------------------

def file_sha256(path: Path) -> str:
    """Return the SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def provenance_block(
    source_path: Path,
    source_sha: str,
    lens_id: str,
    audit_event_id: str,
) -> Dict[str, str]:
    """Build a provenance metadata dictionary for an output file."""
    return {
        "source_file": str(source_path),
        "source_sha256": source_sha,
        "ingestor_lens": lens_id,
        "audit_event_id": audit_event_id,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
    }


# ---------------------------------------------------------------------------
# CSV / XLSX normalization helpers
# ---------------------------------------------------------------------------

def normalize_date(raw: str) -> str:
    """Attempt to parse a date string and return ISO-8601 format."""
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%Y%m%d"):
        try:
            return datetime.strptime(raw.strip(), fmt).date().isoformat()
        except ValueError:
            continue
    raise ValueError(f"Cannot parse date: {raw!r}")


def normalize_amount(raw: Any) -> float:
    """Parse an amount field, stripping currency symbols and commas."""
    if isinstance(raw, (int, float)):
        return float(raw)
    cleaned = str(raw).replace(",", "").replace("$", "").replace("£", "").replace("€", "").strip()
    if cleaned in ("", "-", "N/A"):
        return 0.0
    return float(cleaned)


# ---------------------------------------------------------------------------
# Ledger I/O
# ---------------------------------------------------------------------------

def write_canonical_csv(rows: List[Dict[str, Any]], output_path: Path, provenance: Dict[str, str]) -> None:
    """Write normalized rows to a canonical CSV file, including a provenance header."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        # Write provenance as JSON comment in line 1
        fh.write("# PROVENANCE: " + json.dumps(provenance) + "\n")
        writer = csv.DictWriter(fh, fieldnames=CANONICAL_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_canonical_csv(path: Path) -> List[Dict[str, Any]]:
    """Read a canonical CSV file, skipping provenance comment lines."""
    rows: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as fh:
        reader = csv.DictReader(line for line in fh if not line.startswith("#"))
        for row in reader:
            rows.append(dict(row))
    return rows
