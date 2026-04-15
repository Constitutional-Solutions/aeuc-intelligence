from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Literal, Optional
import hashlib
import json

Status = Literal["success", "failure", "contested", "aborted"]


@dataclass
class AuditEvent:
    """Canonical audit event used for FSOU logging.

    Events are designed to be serialized to JSON and optionally stored
    in hash-chained append-only logs.
    """

    id: str
    timestamp: str
    actor_id: str
    action: str
    category: str
    inputs_hash: str
    outputs_hash: str
    status: Status
    tags: List[str]
    notes: str = ""
    prev_event_hash: Optional[str] = None

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))

    def compute_self_hash(self) -> str:
        """Compute a Blake2b-256 hash of the JSON representation.

        This hash can be used as the `prev_event_hash` for the next event.
        """

        h = hashlib.blake2b(self.to_json().encode("utf-8"), digest_size=32)
        return h.hexdigest()


def _hash_payload(payload: Any) -> str:
    """Hash arbitrary JSON-serializable payload with Blake2b-256."""

    data = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    h = hashlib.blake2b(data, digest_size=32)
    return h.hexdigest()


def make_audit_event(
    *,
    event_id: str,
    actor_id: str,
    action: str,
    category: str,
    inputs: Any,
    outputs: Any,
    status: Status,
    tags: Optional[List[str]] = None,
    notes: str = "",
    prev_event_hash: Optional[str] = None,
) -> AuditEvent:
    """Create a new `AuditEvent` from raw inputs and outputs."""

    now = datetime.now(timezone.utc).isoformat()
    return AuditEvent(
        id=event_id,
        timestamp=now,
        actor_id=actor_id,
        action=action,
        category=category,
        inputs_hash=_hash_payload(inputs),
        outputs_hash=_hash_payload(outputs),
        status=status,
        tags=tags or [],
        notes=notes,
        prev_event_hash=prev_event_hash,
    )


def audit(  # type: ignore[misc]
    *,
    actor_id: str,
    action: str,
    category: str,
    tags: Optional[List[str]] = None,
    notes: str = "",
    event_id_factory=lambda: hashlib.blake2b(
        datetime.now(timezone.utc).isoformat().encode("utf-8"), digest_size=16
    ).hexdigest(),
    prev_event_hash_getter=lambda: None,
    event_sink=lambda event: None,
):
    """Decorator to wrap functions in an AuditEvent.

    Parameters
    ----------
    actor_id: str
        Lens or human ID performing the action.
    action: str
        Short verb phrase describing the action.
    category: str
        High-level category (e.g. "governance", "deployment").
    tags: list[str]
        Optional tags for search and filtering.
    notes: str
        Optional static notes.
    event_id_factory: Callable[[], str]
        Function that generates a unique event ID.
    prev_event_hash_getter: Callable[[], Optional[str]]
        Function returning the hash of the previous event in the chain.
    event_sink: Callable[[AuditEvent], None]
        Function that receives the AuditEvent (e.g. to write to a file or DB).
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            prev_hash = prev_event_hash_getter()
            event_id = event_id_factory()
            try:
                result = func(*args, **kwargs)
                status: Status = "success"
            except Exception as exc:  # noqa: BLE001
                result = {"error": str(exc)}
                status = "failure"
                raise
            finally:
                event = make_audit_event(
                    event_id=event_id,
                    actor_id=actor_id,
                    action=action,
                    category=category,
                    inputs={"args": args, "kwargs": kwargs},
                    outputs=result,
                    status=status,
                    tags=tags,
                    notes=notes,
                    prev_event_hash=prev_hash,
                )
                event_sink(event)

        return wrapper

    return decorator
