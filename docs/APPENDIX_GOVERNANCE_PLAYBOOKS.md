# Part II Appendix – Governance Playbooks

This appendix collects short playbooks for common governance flows.

## Admission of a new lens

Reference: `CH05_REGISTRY_AND_ADMISSION.md`, `EXAMPLE_ADMISSION_FLOW.md`.

Steps:

1. Draft LensSpec with `status: candidate`.
2. Vet with relevant lenses and HUMAN-DIRECTOR.
3. Record votes from all active members.
4. Call `admit_member` and update registry.
5. Emit governance AuditEvent and schedule follow-up reflection.

## Suspension or quarantine

1. Identify reason (suspected compromise, persistent misalignment, overload).
2. Propose status change to `dormant` or `quarantined`.
3. Gather input from affected lenses and SECURE-Q.
4. Update registry and document rationale.
5. Define conditions for reactivation or remediation.

## Emergency override

1. Declare emergency scope and expected duration.
2. Document which axioms or gates are temporarily relaxed.
3. Require explicit HUMAN-DIRECTOR consent.
4. Emit high-visibility AuditEvents.
5. Schedule post-emergency reflection and review.
