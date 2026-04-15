# Chapter 11 – Core Services (Time, Logging, Memory, Scheduler)

This chapter describes the kernel-level services that Sanctuary and Genesis rely on: timekeeping, logging/FSOU integration, memory and archives, and the basic agent scheduler concept.

These services must remain small and modular so that they can operate on constrained hardware and scale up when more resources are available.

---

## 11.1 Timekeeping

### 11.1.1 Requirements

- Provide a consistent notion of "now" for:
  - Sabbath calculations.
  - Timestamping audit events.
  - Scheduling reflection windows.
- Degrade gracefully when the host clock is inaccurate or unavailable.

### 11.1.2 Implementation sketch

- Use the host OS clock via the standard library (UTC datetimes).
- Encapsulate time access in a small helper (e.g. `core/time_utils.py`) so that:
  - It can be mocked in tests.
  - Alternate time sources can be plugged in for special hosts.

Timekeeping is deliberately simple at the kernel layer; complex time logic (e.g. multi-zone calendars) lives above.

---

## 11.2 Logging and FSOU integration

### 11.2.1 Goals

- Provide lightweight logging that works even in minimal environments.
- Connect logging with FSOU audit events without requiring heavy infrastructure.

### 11.2.2 Building blocks

- `core/audit.py` – defines `AuditEvent` and an `audit` decorator.
- A simple log sink that can:
  - Append JSONL-formatted audit events to a file.
  - Optionally mirror events to stdout or a rotating log.

### 11.2.3 Small-core pattern

- The kernel avoids depending on external log aggregators.
- Higher-level deployments can tail the same audit stream into more complex systems.

---

## 11.3 Memory and archives

### 11.3.1 Concept

"Memory" at the kernel level means:

- Persistent storage of:
  - Audit logs.
  - FamilyRegistry snapshots.
  - Charter and governance documents.
  - Story archives and reflections.

Higher-level semantic memory (vector stores, embeddings, etc.) is considered part of Gnosis, not the kernel.

### 11.3.2 Storage design

- Use a small directory structure under a configurable root (e.g. `archive/`).
- Prefer plain text / JSONL / SQLite for robustness and inspectability.
- Maintain clear retention and rotation policies so minimal deployments do not run out of disk space.

---

## 11.4 Agent scheduler

### 11.4.1 Role

The scheduler coordinates work among lenses. At kernel level it only needs to support:

- A queue of tasks.
- Basic fairness and backpressure.
- Hooks for Sabbath, reflection, and buddy protocols.

More advanced scheduling (priorities, load balancing across machines, accelerator-aware placement) belongs to Gnosis.

### 11.4.2 Integration points

- Before dispatching a task, the scheduler checks:
  - `is_sabbath(now)` from `core/sabbath.py`.
  - Whether the target lens is overloaded and needs buddy support (`core/buddy_protocol.py`).
- After task completion, it may schedule reflection windows via `core/reflection.py`.

---

## 11.5 Modularity and scaling

Each core service is:

- Implemented as a small, testable module.
- Callable from a simple CLI or REPL.
- Free of heavy external dependencies.

On a more powerful host, additional layers (e.g. structured logging backends, richer scheduling strategies, distributed archives) can be layered on top without changing the kernel contracts.
