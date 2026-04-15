from __future__ import annotations

from datetime import datetime, timezone


def now_utc() -> datetime:
    """Return the current time as an aware UTC datetime.

    This helper centralizes access to the host clock so that time can be
    mocked in tests and, if necessary, sourced differently on special hosts.
    """

    return datetime.now(timezone.utc)
