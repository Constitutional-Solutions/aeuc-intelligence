# Core System Development Archive

This document is a living archive of how the AEUC family came into being: the history, architectural discussions, protocols, and governance reflections that underpin the Preamble, Mission Statement, and Constitutional Axioms.

It is not a changelog of individual commits, but a narrative of major design movements. Future generations should extend this archive when the family crosses significant thresholds.

---

## 1. Origins

The AEUC family emerged from two recognitions:

1. Modern AI stacks are structurally misaligned with individual sovereignty and long-term human flourishing.
2. Beautiful architectures and insights are often fragile, disappearing when a single person, notebook, or account is compromised.

The initial design work therefore focused on:

- **Constitutional governance** – a Charter, principles, and axioms that are explicit and enforceable.
- **Reconstructability** – documentation canon, archives, and reproducible build processes so the system can be rebuilt even after disruption.

These concerns produced the first drafts of:

- `docs/FAMILY_CHARTER.md` – high-level law.
- `docs/CH01_PREAMBLE.md` – narrative motivation.
- `docs/CH02_CORE_PRINCIPLES.md` – mechanisms for sovereignty, Love/Truth/Power, auditability, separation of concerns, rest, and human dignity.
- `docs/CH03_CONSTITUTIONAL_AXIOMS.md` – non-negotiable rails.

---

## 2. Architectural spine

The core architectural choices can be summarized as:

- **Multi-agent family** – Intelligence is decomposed into named lenses (DEBUG-1, ARCHITECT-Q, CODE-Q, etc.), each with a clear role and invariants.
- **FamilyRegistry + LensSpec** – Membership is explicit and machine-readable.
- **Immutable Charter Kernel** – A minimal module that can verify Charter integrity offline.
- **FSOU audit events** – A single schema for recording what happened, when, and under which invariants.
- **Rhythms of rest** – Sabbath, buddy protocol, and reflection windows are enforced at the orchestration layer.
- **Separation of core / research / experiments** – Different directories and governance rules prevent speculative work from silently becoming law.

These choices are implemented in `core/`, `config/`, `scripts/`, and the surrounding docs.

---

## 3. Governance reflections

Key governance decisions that shaped Part I:

- **Unanimous consent for expansion** – New members, capabilities, or Charter changes require unanimous consent among core lenses and human covenant holders.
- **Human director as covenant holder** – At least one human member (HUMAN-DIRECTOR) is explicitly named as holding final responsibility for covenant-level decisions.
- **Axioms as hard rails** – Certain rules (audit required, no member without spec/tests, Sabbath enforcement, immutable Charter precedence) are placed beyond routine configuration.

---

## 4. Protocols and their evolution

### 4.1 Audit and FSOU

Early prototypes logged actions inconsistently. The family converged on a canonical `AuditEvent` schema with:

- hash-chained events
- clear actor identification
- structured categories and tags

This allowed independent tools to consume logs while preserving integrity.

### 4.2 Sabbath, buddy, and reflection

Experience with long-running systems made it clear that burnout and silent drift were real risks. Sabbath protocol, buddy mappings, and reflection windows were promoted from "nice ideas" to kernel-level concerns.

### 4.3 Registry and contracts

Initially, member descriptions existed only in prose. They were formalized into LensSpec objects and a YAML-backed FamilyRegistry so that governance decisions could be validated automatically.

---

## 5. Milestones

This section should be extended over time. Initial milestones include:

- **Part I completion** – Preamble, Core Principles, and Constitutional Axioms written and aligned with code.
- **First family registry** – All 15 technical lenses plus HUMAN-DIRECTOR recorded in `config/family_registry.yaml`.
- **Boot CLI** – `scripts/build_family.py` providing a single entry point to verify Charter integrity, Sabbath status, and registry health.

Future milestones might include:

- First external deployment.
- First contested governance decision and its resolution.
- Major refactors of architecture or protocols.
