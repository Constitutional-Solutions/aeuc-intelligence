# Chapter 9 – Kernel Overview: Sanctuary · Genesis · Gnosis

This chapter introduces the conceptual structure of the AEUC kernel and how it supports modular, resource-frugal deployments.

---

## 9.1 Naming: Sanctuary, Genesis, Gnosis

The kernel is organized into three conceptual layers:

- **Sanctuary** – The minimal, always-on safety core.
  - Responsibilities:
    - Charter integrity verification (Charter kernel).
    - Basic timekeeping.
    - Minimal logging and FSOU hooks.
    - Knowledge of which lenses exist (FamilyRegistry).
  - Properties: tiny footprint, no external dependencies beyond the host OS and filesystem.

- **Genesis** – The boot and initialization layer.
  - Responsibilities:
    - Discover the environment (host capabilities, storage, network).
    - Run environment checks (e.g. file layout, available RAM/CPU, optional accelerator presence).
    - Call Sanctuary functions to verify Charter and registry.
    - Transition from "cold" to "running" state.

- **Gnosis** – The higher-order reasoning and orchestration surface.
  - Responsibilities:
    - Provisioning and task orchestration (ORCHEST-Q, provisioner design).
    - Agent scheduling and coordination across lenses.
    - Integration with external tools, models, and substrates.
  - Properties: can be scaled up or down depending on hardware; can be replaced or extended without changing Sanctuary or Genesis.

This separation ensures that even in very constrained environments, Sanctuary and a minimal slice of Genesis can operate, while Gnosis can be selectively enabled where resources permit.

---

## 9.2 Modular design for constrained hardware

The kernel is designed to:

- **Boot from simple storage** (e.g. USB drive) on machines with as little as 4 GB of RAM.
- **Only load what is needed** for the current mode of operation.
- **Degrade gracefully** when optional components (network, accelerators, large models) are unavailable.

Patterns that support this:

- Clear module boundaries (e.g. `core/charter_kernel.py`, `core/family_kernel.py`, `core/sabbath.py`, `core/reflection.py`).
- Configuration-driven enabling of features: core kernel first, then optional layers.
- Avoiding heavy frameworks at the kernel level; use standard libraries and small, auditable helpers.

---

## 9.3 Relationship to existing modules

The current repository already contains pieces of each layer:

- **Sanctuary-building blocks**
  - `core/charter_kernel.py` – immutable Charter hash and verification.
  - `core/family_registry.py` + `config/family_registry.yaml` – membership knowledge.
  - `core/audit.py` – canonical FSOU event format and decorator.

- **Genesis-building blocks**
  - `core/family_kernel.py` – `check_kernel_status()` tying together Charter verification, Sabbath status, and active members.
  - `scripts/build_family.py` – a simple boot CLI.

- **Gnosis-building blocks**
  - `docs/PROVISIONER_DESIGN.md` – how to route tasks and apply gates.
  - The definitions of lenses like ORCHEST-Q and SECURE-Q.

Part III’s remaining chapters will refine these into a clean, modular kernel that can be instantiated on different substrates without rewriting core logic.
