from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Iterable


@dataclass
class ReflectionWindow:
    lens_id: str
    start: datetime
    end: datetime
    kind: str  # e.g. "sabbath", "micro"


def schedule_weekly_sabbath_reflection(
    *,
    lens_id: str,
    sabbath_start: datetime,
    duration_hours: int = 4,
) -> ReflectionWindow:
    """Schedule a longer reflection session aligned with Sabbath."""

    return ReflectionWindow(
        lens_id=lens_id,
        start=sabbath_start,
        end=sabbath_start + timedelta(hours=duration_hours),
        kind="sabbath",
    )


def reflection_ratio(total_active_hours: float, reflection_hours: float) -> float:
    """Return the fraction of time spent in reflection.

    Used to gauge how close a lens is to the 1/3 reflection norm.
    """

    if total_active_hours <= 0:
        return 0.0
    return reflection_hours / total_active_hours


def meets_reflection_norm(total_active_hours: float, reflection_hours: float) -> bool:
    """Return True if the reflection ratio is at least ~1/3."""

    return reflection_ratio(total_active_hours, reflection_hours) >= 1.0 / 3.0


def total_reflection_hours(windows: Iterable[ReflectionWindow]) -> float:
    """Compute total reflection hours from a sequence of windows."""

    total = 0.0
    for w in windows:
        total += (w.end - w.start).total_seconds() / 3600.0
    return total
