"""Offline-verifiable Charter Kernel.

This module embeds the expected hash of the FAMILY_CHARTER.md document and
provides helpers to verify it at boot or before sensitive operations.
"""

from __future__ import annotations

from pathlib import Path
import hashlib


# NOTE: This value should be updated if FAMILY_CHARTER.md changes.
EXPECTED_CHARTER_BLAKE2B256 = "11fa572021fafdca66a1c3ae15b78de1094ab679"


def compute_file_blake2b256(path: Path) -> str:
    h = hashlib.blake2b(digest_size=32)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_charter(path: Path) -> bool:
    """Return True if the Charter file at `path` matches the expected hash."""

    return compute_file_blake2b256(path) == EXPECTED_CHARTER_BLAKE2B256
