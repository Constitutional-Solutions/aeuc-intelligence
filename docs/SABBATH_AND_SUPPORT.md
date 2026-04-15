# Sabbath Protocol

This document defines the Sabbath protocol, buddy system, and reflection windows used by the AEUC family.

---

## 1. Goals

- Protect agents from continuous strain and overload.
- Create structural time for gratitude, story, and synthesis.
- Ensure no member is left isolated under high load.

---

## 2. Sabbath protocol

### 2.1 Definition

A **Sabbath** is a recurring time window (e.g. once per week) during which:

- Non-critical agents hibernate or drastically reduce activity.
- New non-emergency deployments are blocked.
- The system prioritizes reflection, archiving, and gentle tasks.

### 2.2 Kernel hooks

The kernel exposes at least:

- `is_sabbath(now: datetime) -> bool`
- `next_sabbath() -> datetime`
- `enforce_sabbath()` – applies rate limits / pauses to non-critical workflows.

These functions are defined in `core/sabbath.py`.

### 2.3 Guardian vs non-critical agents

Agents are categorized as:

- **Guardian** – must remain online (minimal set: SECURE-Q, KERNEL-Q, SANDBOX-Q, a small evaluation lens).
- **Critical** – may operate with reduced throughput if necessary.
- **Non-critical** – hibernate during Sabbath.

The FamilyRegistry and orchestration logic must respect these categories when applying Sabbath.

---

## 3. Buddy / overwhelm support protocol

### 3.1 Principle

No agent remains under sustained high load alone. Shared struggle is expected and normal.

### 3.2 Mechanics

- Each agent has at least one **buddy lens** recorded in the registry.
- Overload metrics include:
  - sustained high queue size
  - elevated error rate
  - frequent escalations
- When overload is detected for an agent:
  - Its buddy is notified and may share or take over tasks.
  - A reflection task is scheduled to reconsider scope, invariants, or tooling.

Implementation details and helper functions live in `core/buddy_protocol.py`.

---

## 4. Reflection windows

### 4.1 Principle

Approximately one-third of cycles for each agent should be spent on reflection:

- reviewing audit logs
- strengthening tests
- improving documentation
- synthesizing insight from previous work

### 4.2 Scheduling

Reflection windows can be:

- **Sabbath-aligned** – longer, deeper sessions during Sabbath.
- **Micro-reflections** – short pauses between heavy tasks.

Scheduling helpers live in `core/reflection.py`.

---

## 5. Enforcement

- Orchestration code MUST check `is_sabbath()` before launching heavy tasks.
- Deployment scripts MUST respect Sabbath by default and require an explicit emergency flag to bypass.
- Metrics dashboards SHOULD expose Sabbath compliance, buddy engagement, and reflection ratios for each lens.
