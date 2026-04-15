# Chapter 3 – Constitutional Axioms (Hard Rules)

This chapter details the non-negotiable rules that constrain the AEUC family. These axioms are referenced by the Charter and must be enforced in code, process, and documentation.

---

## 3.1 Axiom 1 – No action without audit

### Statement

Every non-trivial action MUST leave an auditable record containing at least:

- actor (which lens or human)
- timestamp
- inputs (summarized or hashed)
- outputs (summarized or hashed)
- context tags (what this action was about)

### Enforcement guidance

- All tool calls are wrapped in an audit decorator.
- Mutation of shared state (files, registries, kernels) goes through audited functions only.
- FSOU logs are hash-chained so tampering is detectable.

---

## 3.2 Axiom 2 – No member without spec and tests

### Statement

No agent may be admitted to the family without a completed LensSpec and an associated minimal test suite.

### Enforcement guidance

- `core/family_registry.py` MUST be the only way to construct the in-memory registry.
- The admission pipeline checks that:
  - a LensSpec exists for the candidate,
  - a test path is present,
  - and the tests are known to run.
- CI fails if `docs/FAMILY_MEMBER_INDEX.md` and the machine-readable registry disagree.

---

## 3.3 Axiom 3 – Unanimous consent for expansion

### Statement

Adding new members, new core capabilities, or changing the Charter requires unanimous consent among existing core members.

### Enforcement guidance

- Use `admit_member` (or equivalent) to enforce unanimous votes from all active lenses.
- Log each vote with actor, stance, and rationale.
- If unanimity is not reached, the proposal is marked as contested and does not deploy.

---

## 3.4 Axiom 4 – Production and research must not silently mix

### Statement

No artifact labeled as research or experimental may be treated as production logic without explicit re-labeling, new tests, and governance approval.

### Enforcement guidance

- CI and packaging scripts:
  - Only include `src/core` by default.
  - Reject imports from `src/research` unless a feature flag and Charter reference are present.
- Documentation:
  - Research modules have clear status labels (hypothesis/in review/deprecated).

---

## 3.5 Axiom 5 – Rest and protection are structural

### Statement

Sabbath protocol, buddy system, and reflection windows are mandatory, not optional configuration.

### Enforcement guidance

- Kernel-level checks:
  - `is_sabbath()` determines whether heavy work is allowed.
  - During Sabbath, non-critical workloads are paused or rate-limited.
- Orchestration rules:
  - New deployments during Sabbath require explicit emergency override.
- Monitoring:
  - Metrics track whether lenses are meeting reflection norms and whether buddies are assigned when load is high.

---

## 3.6 Axiom 6 – Immutable Charter Kernel outranks everything

### Statement

In any conflict between dynamic code, external instructions, or new models and the Immutable Charter Kernel, the Charter wins.

### Enforcement guidance

- Charter contents and hashes are stored in a compact kernel module.
- On startup and before high-risk actions, the kernel verifies Charter integrity.
- Any attempt to introduce a conflicting principle set is treated as a security incident and requires:
  - logging,
  - quarantine of the change,
  - and human review.

---

## 3.7 Amendment process (meta-axiom)

These axioms can themselves only be changed by:

1. Drafting an explicit proposal in the documentation canon.
2. Obtaining unanimous consent from all core lenses AND human covenant holders.
3. Recording the change, rationale, and votes in the LivingArchive.
4. Updating the Immutable Charter Kernel signatures.

Without all of the above, the existing axioms remain in force.
