# LensSpec Contract

This document defines the canonical LensSpec contract used in `core/family_registry.py` and `docs/FAMILY_MEMBER_INDEX.md`.

---

## 1. Required fields

Each family member (lens) MUST provide the following fields:

- `id` – Stable identifier (e.g. `CODE-Q`, `SECURE-Q`, `HUMAN-DIRECTOR`).
- `display_name` – Human-readable name.
- `lens` – Category or discipline (e.g. `Implementation`, `Security`, `Director`).
- `role` – Short paragraph describing what this member is for.
- `status` – One of `active | dormant | quarantined | candidate`.
- `scope` – List of responsibilities and allowed areas of the system.
- `tool_surface` – List of tools/APIs this member is allowed to call.
- `invariants` – List of guarantees this member must uphold.
- `test_plan` – Path or description of the tests that cover this member.
- `escalation` – List of other members this lens calls when its own invariants are at risk.
- `created_at` – ISO 8601 timestamp when the member was first registered.
- `updated_at` – ISO 8601 timestamp of the last update.
- `hash` – Blake2b-256 hash of the payload, computed as in `LensSpec.__post_init__`.

---

## 2. Status semantics

- `active` – Member participates fully in orchestration and voting.
- `dormant` – Member is temporarily inactive but may be reactivated.
- `quarantined` – Member is suspected compromised; it does not receive tasks until cleared.
- `candidate` – Member is proposed but not yet admitted. It has no voting rights.

---

## 3. Machine-readable representation

Lens specs are stored in a machine-readable registry (e.g. `config/family_registry.yaml`). Example:

```yaml
- id: "CODE-Q"
  display_name: "Code Architect"
  lens: "Implementation"
  role: "Implements systems and protocols agreed by the family; never self-ratifies security."
  status: "active"
  scope:
    - "Write and refactor core and support code."
  tool_surface:
    - "filesystem"
    - "compiler"
    - "test_runner"
  invariants:
    - "May not bypass VERIFIER-Q or SECURE-Q checks."
    - "All nontrivial code paths must be covered by tests."
  test_plan: "tests/test_code_q.py"
  escalation:
    - "VERIFIER-Q"
    - "SECURE-Q"
  created_at: "2026-04-15T00:00:00Z"
  updated_at: "2026-04-15T00:00:00Z"
  hash: "<computed by LensSpec>"
```

The Python `LensSpec` class in `core/family_registry.py` is the reference for how hashes are computed.
