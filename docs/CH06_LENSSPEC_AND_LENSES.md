# Chapter 6 – LensSpec and Specialist Lenses

This chapter details the LensSpec contract and explains why each of the core specialist lenses is considered necessary rather than optional.

---

## 6.1 LensSpec schema

Every member (lens) has a LensSpec defined in `core/family_registry.py` and documented in `docs/LENSSPEC_CONTRACT.md`.

Required fields:

- `id` – stable identifier (e.g. `CODE-Q`).
- `display_name` – human-readable name.
- `lens` – category or discipline (Implementation, Security, Director, etc.).
- `role` – what this member is for.
- `status` – `active | dormant | quarantined | candidate`.
- `scope` – responsibilities and allowed areas.
- `tool_surface` – tools and APIs this lens may call.
- `invariants` – guarantees that must always hold.
- `test_plan` – how this lens is tested.
- `escalation` – who it calls when its invariants are at risk.
- `created_at`, `updated_at` – timestamps.
- `hash` – Blake2b-256 hash computed from the other fields.

The hash allows the registry to detect tampering or accidental edits.

---

## 6.2 Specialist lenses (why each matters)

The family currently defines fifteen technical lenses plus HUMAN-DIRECTOR. Each exists to prevent specific failure modes:

- **DEBUG-1 – Debugging Sentinel**
  - Purpose: Make failures observable and understandable.
  - Without it: Errors are suppressed or overlooked, hiding drift and regressions.

- **ARCHITECT-Q – System Architect**
  - Purpose: Maintain a coherent big-picture design.
  - Without it: Local optimizations conflict and the system fragments.

- **CODE-Q – Code Implementer**
  - Purpose: Turn designs into running code.
  - Without it: Architecture never becomes reality.

- **VERIFIER-Q – Verification Lens**
  - Purpose: Ensure implementations behave as specified.
  - Without it: Bugs and regressions ship unchecked.

- **OPTIMIZER-Q – Optimizer**
  - Purpose: Improve performance safely.
  - Without it: The system becomes slow and resource-hungry, or unsafe optimizations creep in.

- **KERNEL-Q – Kernel Steward**
  - Purpose: Guard the minimal trusted core.
  - Without it: Kernel changes risk breaking invariants system-wide.

- **BUILD-Q – Build System Lens**
  - Purpose: Assemble artifacts reproducibly.
  - Without it: Builds are ad hoc and unreproducible.

- **SECURE-Q – Security Lens**
  - Purpose: Defend against adversaries and enforce security policy.
  - Without it: Attack surfaces grow unchecked.

- **REPRO-Q – Reproducibility Lens**
  - Purpose: Make results and builds repeatable.
  - Without it: Bugs and behaviors cannot be reproduced or studied.

- **PKG-Q – Packaging Lens**
  - Purpose: Create distributable artifacts tied to auditable builds.
  - Without it: Distribution is messy and prone to version confusion.

- **ABI-Q – ABI Guardian**
  - Purpose: Prevent breaking changes to public interfaces.
  - Without it: Downstream consumers silently break.

- **SANDBOX-Q – Sandbox Orchestrator**
  - Purpose: Contain untrusted code.
  - Without it: Experiments risk compromising the entire system.

- **EVAL-Q – Evaluation Lens**
  - Purpose: Measure behavior and progress.
  - Without it: The family cannot tell if changes are improvements.

- **HARDWARE-Q – Hardware Interface Lens**
  - Purpose: Manage physical resources.
  - Without it: Overheating, throttling, or hardware-level bugs may go unnoticed.

- **ORCHEST-Q – Orchestrator**
  - Purpose: Coordinate tasks across lenses and enforce gates.
  - Without it: Work is ad hoc and gate checks are inconsistent.

- **HUMAN-DIRECTOR – Human Director**
  - Purpose: Hold the covenant and embody human judgment.
  - Without it: The system risks drifting away from human values.

Each lens plugs a specific gap; removing any one opens a corresponding class of failure modes.
