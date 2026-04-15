# Glossary

This glossary defines key terms used throughout the AEUC family canon.

---

## A

**AEUC family** – The governed multi-agent system described in this repository, built around a Charter, family registry, and kernel.

**AuditEvent** – Canonical FSOU event capturing who acted, when, with which inputs and outputs, and under which invariants; see `docs/AUDIT_EVENTS.md`.

---

## C

**Charter** – The core constitutional document defining mission, principles, and axioms; see `docs/FAMILY_CHARTER.md`.

**Charter kernel** – Minimal module embedding the Charter hash and verifying its integrity; see `core/charter_kernel.py`.

**Council (family council)** – Structured conversation among lenses and human members to evaluate proposals, often using the Love/Truth/Power geometry.

---

## F

**FamilyRegistry** – Machine-readable list of family members (lenses and humans), implemented in `core/family_registry.py` and `config/family_registry.yaml`.

**FSOU (Full State of Understanding)** – The family’s audit logging concept: a hash-chained record of important events over time.

---

## G

**Gate** – A condition that must be satisfied before proceeding (membership, capability, deployment); see `docs/CH07_VOTING_AND_GATES.md`.

---

## L

**Lens** – A specialized member of the family with a clearly defined role and invariants (e.g. CODE-Q, SECURE-Q).

**LensSpec** – The contract describing a lens: fields such as id, role, status, scope, invariants, and hash; see `core/family_registry.py` and `docs/LENSSPEC_CONTRACT.md`.

**Love / Truth / Power** – The three primary axes of value used to classify decisions and proposals; see `docs/CH02_CORE_PRINCIPLES.md`.

---

## M

**Member** – Any human or agent lens registered in the FamilyRegistry.

---

## R

**Reflection window** – Time reserved for review, synthesis, and strengthening tests/documentation; tracked via `core/reflection.py`.

**Research track** – Experimental modules and documents not yet part of production law; lives under `src/research/` and is governed by separation rules in Part I.

---

## S

**Sabbath** – Recurring rest window in which non-critical work is paused and reflection is prioritized; see `docs/SABBATH_AND_SUPPORT.md` and `core/sabbath.py`.

**Sandbox** – Constrained environment for running untrusted code; coordinated by SANDBOX-Q.

---

## T

**Tool surface** – The set of tools and APIs a given lens is allowed to call.

**Threat model** – Documented analysis of assets, adversaries, and mitigations; see `docs/THREAT_MODEL.md`.
