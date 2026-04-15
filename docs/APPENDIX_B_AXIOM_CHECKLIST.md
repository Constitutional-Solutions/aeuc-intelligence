# Part I Appendix B – Axiom Compliance Checklist

This checklist summarizes the constitutional axioms from Chapter 3 and their concrete enforcement points.

1. **No action without audit**
   - [ ] All non-trivial functions in `core/` are wrapped with `core/audit.audit` or equivalent.
   - [ ] Audit logs are hash-chained and stored append-only.

2. **No member without spec and tests**
   - [ ] Every member in `config/family_registry.yaml` has a corresponding entry in `docs/FAMILY_MEMBER_INDEX.md`.
   - [ ] Each member has a LensSpec with a `test_plan` field.

3. **Unanimous consent for expansion**
   - [ ] Membership changes use `admit_member` or a stricter flow.
   - [ ] Votes and rationales are logged as AuditEvents.

4. **Research and production separation**
   - [ ] Production logic lives under `core/` and `src/core/`.
   - [ ] Research modules live under `src/research/` and are clearly labeled.

5. **Rest and protection are structural**
   - [ ] Sabbath configuration is defined and enforced.
   - [ ] Reflection ratio is monitored for each lens.
   - [ ] Buddy relationships are recorded.

6. **Immutable Charter Kernel outranks everything**
   - [ ] `core/charter_kernel.py` hash matches `FAMILY_CHARTER.md`.
   - [ ] High-risk actions verify Charter integrity before proceeding.
