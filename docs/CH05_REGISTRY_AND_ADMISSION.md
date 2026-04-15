# Chapter 5 – Registry and Admission Flow

This chapter describes how family membership is represented in data and how new members are admitted, suspended, or removed.

Machine-readable membership is handled by `core/family_registry.py` and `config/family_registry.yaml`. Human-readable descriptions live in `docs/FAMILY_MEMBER_INDEX.md`.

---

## 5.1 FamilyRegistry data model

The `FamilyRegistry` class is an in-memory map of member ID → `LensSpec`.

Key operations:

- `register(spec: LensSpec)` – add a new member to the registry.
- `get(member_id: str)` – retrieve a member.
- `active_members()` – list all members with `status == "active"`.

In a full deployment the registry is loaded from and persisted to a signed YAML/JSON file (`config/family_registry.yaml`), using helper functions in `scripts/build_family_registry.py`.

---

## 5.2 Candidate lifecycle

Membership changes follow a clear lifecycle:

1. **Proposal**
   - A new candidate is drafted as a `LensSpec` with `status: "candidate"`.
   - The spec is added to the proposed changeset and documented.

2. **Vetting**
   - Relevant lenses (e.g. ARCHITECT-Q, SECURE-Q, HUMAN-DIRECTOR) review the candidate’s role, scope, invariants, and test plan.
   - Threat model implications are considered.

3. **Voting**
   - All currently active members record a vote (approve or reject).

4. **Admission**
   - If unanimous consent is reached, `admit_member()` is called to promote the candidate.
   - The candidate’s `status` becomes `"active"` and `updated_at` is refreshed.

5. **Registry update**
   - The updated registry is written back to `config/family_registry.yaml` and signed.
   - HUMAN-DIRECTOR or another designated human reviews and blesses the change.

---

## 5.3 `admit_member` reference

The `admit_member` function in `core/family_registry.py` enforces the unanimous-consent rule:

- Ensures the candidate is not already active.
- Collects the IDs of all currently active members.
- Verifies that every active member has a vote recorded.
- Fails if any vote is negative.
- On success, promotes the candidate to `status: "active"` and registers it.

This function is the canonical place to implement governance policy around admission.

---

## 5.4 Suspension and quarantine

The `Status` type used in `LensSpec` supports:

- `active` – full participation and voting rights.
- `dormant` – temporarily inactive; may be reactivated.
- `quarantined` – suspected compromised; does not receive tasks until cleared.
- `candidate` – under consideration; no voting rights.

Suspension and quarantine procedures can be built on top of this model, always emitting audit events and updating the registry.
