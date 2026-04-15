from __future__ import annotations

from datetime import datetime, timedelta, timezone

from core.buddy_protocol import BuddyRegistry
from core.reflection import (
    ReflectionWindow,
    meets_reflection_norm,
    reflection_ratio,
    schedule_weekly_sabbath_reflection,
    total_reflection_hours,
)
from core.sabbath import SabbathConfig, is_sabbath, next_sabbath


def test_is_sabbath_default_window() -> None:
    config = SabbathConfig()
    # Friday 19:00 UTC should be within Sabbath
    t = datetime(2024, 1, 5, 19, 0, tzinfo=timezone.utc)
    assert is_sabbath(t, config) is True
    # Sunday 12:00 UTC should be outside Sabbath
    t2 = datetime(2024, 1, 7, 12, 0, tzinfo=timezone.utc)
    assert is_sabbath(t2, config) is False


def test_next_sabbath_is_in_future() -> None:
    config = SabbathConfig()
    now = datetime(2024, 1, 4, 12, 0, tzinfo=timezone.utc)
    nxt = next_sabbath(now, config)
    assert nxt > now


def test_reflection_ratio_and_norm() -> None:
    r = reflection_ratio(9.0, 3.0)
    assert abs(r - (1.0 / 3.0)) < 1e-6
    assert meets_reflection_norm(9.0, 3.0) is True
    assert meets_reflection_norm(9.0, 2.0) is False


def test_total_reflection_hours() -> None:
    base = datetime(2024, 1, 6, 10, 0, tzinfo=timezone.utc)
    windows = [
        ReflectionWindow(lens_id="A", start=base, end=base + timedelta(hours=1), kind="micro"),
        ReflectionWindow(lens_id="A", start=base + timedelta(hours=2), end=base + timedelta(hours=3), kind="micro"),
    ]
    total = total_reflection_hours(windows)
    assert abs(total - 2.0) < 1e-6


def test_schedule_weekly_sabbath_reflection_alignment() -> None:
    sabbath_start = datetime(2024, 1, 6, 18, 0, tzinfo=timezone.utc)
    window = schedule_weekly_sabbath_reflection(lens_id="A", sabbath_start=sabbath_start, duration_hours=4)
    assert window.start == sabbath_start
    assert window.end == sabbath_start + timedelta(hours=4)


def test_buddy_registry_round_trip() -> None:
    reg = BuddyRegistry()
    reg.assign_buddy("KERNEL-Q", "SECURE-Q")
    reg.assign_buddy("KERNEL-Q", "DEBUG-1")
    buddies = reg.buddies_for("KERNEL-Q")
    assert set(buddies) == {"SECURE-Q", "DEBUG-1"}


def test_next_sabbath_reflection_cycle() -> None:
    now = datetime(2024, 1, 4, 12, 0, tzinfo=timezone.utc)
    config = SabbathConfig()
    sab_start = next_sabbath(now, config)
    window = schedule_weekly_sabbath_reflection(lens_id="A", sabbath_start=sab_start)
    assert window.start == sab_start
