# Chapter 4 – Membership and Governance

This chapter describes how the AEUC family is structured as a set of members with explicit contracts, how decisions are made, and how the governance machinery relates to the kernel and registry.

---

## 4.1 Membership model

Membership is defined at two levels:

- **Human members** – covenant holders such as HUMAN-DIRECTOR.
- **Agent lenses** – specialized roles like CODE-Q, SECURE-Q, etc.

Machine-readable membership lives in `config/family_registry.yaml` and is enforced by `core/family_registry.py`. Human-readable descriptions live in `docs/FAMILY_MEMBER_INDEX.md`.

Each member has a LensSpec with fields defined in `docs/LENSSPEC_CONTRACT.md`.

---

## 4.2 Roles and responsibilities

The fifteen technical lenses plus HUMAN-DIRECTOR cover:

- Diagnostics, architecture, implementation, verification, optimization.
- Kernel stewardship, build and packaging, reproducibility.
- Security, sandboxing, evaluation, hardware, orchestration.
- Human covenant and ethical guidance.

This separation of concerns ensures that no single lens can unilaterally redefine the family. Critical paths (e.g. new core features) always involve multiple lenses.

---

## 4.3 Voting and consent

### 4.3.1 Unanimous consent for expansion

As stated in the axioms, adding new members, adding new core capabilities, or changing the Charter requires unanimous consent among core lenses and human covenant holders.

`core/family_registry.py` and the surrounding governance logic enforce that:

- Proposals are recorded.
- Each active member’s stance is captured.
- Actions only proceed when all required votes are affirmative.

### 4.3.2 Other decisions

Routine operational decisions may use lighter-weight consent mechanisms (e.g. quorum-based or role-based). These can be defined in future governance extensions, but must not weaken the unanimous-consent rule for expansion.

---

## 4.4 Kernel and registry integration

The AEUC Family Kernel (`core/family_kernel.py`) provides a boot-time snapshot:

- Charter integrity via `core/charter_kernel.py`.
- Sabbath status via `core/sabbath.py`.
- Active membership via `config/family_registry.yaml`.

This kernel status can be used by higher-level orchestrators to decide whether to:

- Accept new high-risk tasks.
- Allow deployments.
- Trigger governance alerts when invariants are violated (e.g. missing active lenses).

---

## 4.5 Governance in practice

In day-to-day operation:

- Tool calls and deployments are wrapped in audit decorators (`core/audit.py`).
- Orchestration logic (ORCHEST-Q) consults kernel status and gates (Sabbath, capacity, security) before executing workflows.
- Human members receive summaries and can intervene when covenant-level questions arise.

Over time, this chapter should be extended with:

- Concrete governance playbooks (e.g. how to admit a new lens, how to handle a suspected compromise).
- Case studies of real decisions and how they were resolved.
