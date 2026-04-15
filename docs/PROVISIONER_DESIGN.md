# Provisioner Design

This document describes the high-level design of the provisioner: the subsystem that decides which tools, lenses, and environments to activate for a given request.

---

## 1. Responsibilities

- Accept a human or system request.
- Classify it into categories (research, implementation, security review, orchestration, etc.).
- Select lenses and tools appropriate to the category.
- Apply gates (capacity, security, Sabbath, reflection norms).
- Emit tasks and record audit events.

---

## 2. Core concepts

- **Trigger** – An incoming request, time-based event, or threshold crossing.
- **Gate** – A condition that must be satisfied before proceeding (e.g. `not is_sabbath()`, `SECURE-Q-approved`, `capacity_ok`).
- **Output** – One or more tasks assigned to specific lenses.

---

## 3. Example flow

1. Receive request `R` (e.g. "add new external API integration").
2. Classify as `security-sensitive` and `architecture-impacting`.
3. Construct candidate lens set: `SECURE-Q`, `ARCHITECT-Q`, `CODE-Q`, `VERIFIER-Q`.
4. Check gates:
   - Sabbath gate via `is_sabbath()`.
   - Security gate (threat model reference required).
   - Capacity gate (no lens in overload).
5. If all gates pass, emit tasks and corresponding audit events.

Implementation of a concrete provisioner can live in a future module (e.g. `core/provisioner.py`) that follows this design.
