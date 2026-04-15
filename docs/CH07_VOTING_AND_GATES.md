# Chapter 7 – Voting Policy and Gates

This chapter explains how the family makes decisions and how gate checks protect critical transitions.

---

## 7.1 Unanimous consent as default

For high-impact changes—new members, new core capabilities, Charter amendments—the default policy is **unanimous consent** among all active core lenses and human covenant holders.

Rationale:

- Each lens sees different risks (security, performance, ethics, etc.).
- Requiring unanimity ensures that no perspective is silently overruled.

`admit_member()` in `core/family_registry.py` encodes this rule for membership changes.

---

## 7.2 When supermajorities are allowed

Some decisions may use lighter requirements, for example:

- Operational parameter tuning.
- Non-core feature toggles.

These may be governed by supermajority or role-based consent (e.g. ARCHITECT-Q + SECURE-Q + HUMAN-DIRECTOR). Such policies must be:

- Documented explicitly.
- Never used for Charter changes or new core abilities.

---

## 7.3 Gate types

The family uses several types of gates:

- **Membership gates** – control who can join, be suspended, or be quarantined. Implemented via registry status and unanimous voting.

- **Capability gates** – control which lenses may exercise certain powers (e.g. network access, model loading, kernel changes). These are enforced via `tool_surface`, invariants, and SECURE-Q policies.

- **Deployment gates** – control whether new code or configurations can be deployed. These involve:
  - Sabbath gates (`is_sabbath()`),
  - Security gates (threat model reference and SECURE-Q approval),
  - Capacity gates (no overloaded lenses).

The provisioner design in `docs/PROVISIONER_DESIGN.md` describes how these gates combine for real workflows.

---

## 7.4 Family council procedures and reflection cycles

Family councils are structured conversations among lenses and human members.

Typical flow:

1. Present proposal and context.
2. Walk the Love/Truth/Power geometry: which axis and sector is primary?
3. Hear each lens’s perspective.
4. Identify risks and mitigations.
5. Call for votes.
6. Schedule reflection tasks to review outcomes after deployment.

Reflection cycles tie back to:

- Sabbath windows (`docs/SABBATH_AND_SUPPORT.md`).
- Reflection windows and norms (`core/reflection.py`).

Councils and reflection are where the Charter’s values are translated into lived practice.
