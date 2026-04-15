from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Literal


Weekday = Literal[0, 1, 2, 3, 4, 5, 6]  # Monday=0 .. Sunday=6


@dataclass
class SabbathConfig:
    """Configuration for Sabbath scheduling.

    By default, Sabbath runs from Friday 18:00 UTC to Saturday 18:00 UTC.
    """

    start_weekday: Weekday = 4  # Friday
    start_hour_utc: int = 18
    duration_hours: int = 24


def is_sabbath(now: datetime, config: SabbathConfig | None = None) -> bool:
    """Return True if `now` falls within the configured Sabbath window."""

    if config is None:
        config = SabbathConfig()

    now_utc = now.astimezone(timezone.utc)
    # Find the most recent Sabbath start
    days_since_start = (now_utc.weekday() - config.start_weekday) % 7
    last_start_date = now_utc.date() - timedelta(days=days_since_start)
    last_start = datetime(
        year=last_start_date.year,
        month=last_start_date.month,
        day=last_start_date.day,
        hour=config.start_hour_utc,
        tzinfo=timezone.utc,
    )
    next_start = last_start + timedelta(days=7)

    window_start = last_start
    window_end = window_start + timedelta(hours=config.duration_hours)

    # If we are before the last_start in this week, use the previous week's window
    if now_utc < window_start:
        window_start = last_start - timedelta(days=7)
        window_end = window_start + timedelta(hours=config.duration_hours)

    return window_start <= now_utc < window_end


def next_sabbath(now: datetime, config: SabbathConfig | None = None) -> datetime:
    """Return the start time of the next Sabbath after `now`."""

    if config is None:
        config = SabbathConfig()

    now_utc = now.astimezone(timezone.utc)

    days_until_start = (config.start_weekday - now_utc.weekday()) % 7
    candidate_date = now_utc.date() + timedelta(days=days_until_start)
    candidate_start = datetime(
        year=candidate_date.year,
        month=candidate_date.month,
        day=candidate_date.day,
        hour=config.start_hour_utc,
        tzinfo=timezone.utc,
    )

    if candidate_start <= now_utc:
        candidate_start += timedelta(days=7)

    return candidate_start
