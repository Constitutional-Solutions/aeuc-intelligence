# Audit Events and FSOU Schema

This document defines the canonical `AuditEvent` structure and how audit logging (FSOU – Full State of Understanding) is used across the AEUC family.

---

## 1. Purpose

Audit events are the backbone of the family’s integrity. Every non-trivial action must leave an event so that future readers can answer:

- Who acted?
- When did they act?
- With which inputs and assumptions?
- What outputs were produced?
- Under which invariants and protocols?

---

## 2. Canonical AuditEvent fields

All audit events share a common schema, independent of where they are stored:

- `id` – Stable identifier for this event (radix/glyph-based if desired).
- `timestamp` – ISO 8601 UTC timestamp.
- `actor_id` – Lens or human ID (e.g. `CODE-Q`, `SECURE-Q`, `HUMAN-DIRECTOR`).
- `action` – Short verb phrase (e.g. `deploy_module`, `run_tests`, `admit_member`).
- `category` – High-level category (`governance`, `deployment`, `security`, `task`, `experiment`, etc.).
- `inputs_hash` – Blake2b-256 hash of the serialized inputs or arguments.
- `outputs_hash` – Blake2b-256 hash of the serialized outputs or results.
- `status` – `success | failure | contested | aborted`.
- `tags` – List of free-form tags for search (e.g. `sabbath`, `threat-model`, `migration`).
- `notes` – Optional human-readable summary.
- `prev_event_hash` – Hash of the previous event in the chain (or null for the first), to support hash-chained integrity.

Implementations may add more fields, but these MUST be present for all FSOU-compliant events.

---

## 3. Hash chaining

Audit logs are stored as an ordered sequence. For each event:

- `prev_event_hash` holds the Blake2b-256 hash of the serialized previous event.
- A verifier can walk the chain and recompute hashes to detect tampering.

This provides strong integrity guarantees even when logs are stored on untrusted storage.

---

## 4. Storage formats

The recommended storage formats are:

- **JSON Lines** – one `AuditEvent` JSON object per line.
- **SQLite** – a simple table with columns matching the fields above.

Both formats can be used side by side. The important property is that events are append-only and hash-chained.

---

## 5. Usage patterns

- All public APIs in `core/` should be wrapped with the audit decorator from `core/audit.py`.
- Governance actions (membership changes, Charter amendments) MUST emit audit events.
- Security-critical operations (network access, key management, sandbox escapes) MUST emit audit events with category `security`.

See `core/audit.py` for the reference implementation.
