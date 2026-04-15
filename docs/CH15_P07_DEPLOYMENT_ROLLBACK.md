# Pattern P07 – Controlled Deployment and Rollback

## Template fields

| Field | Value |
|---|---|
| Name | Controlled Deployment and Rollback |
| Domain / primary axis | Safety-Critical · Love · Truth |
| Intent | Execute an approved change in a controlled, monitored, and reversible way; maintain a verified rollback path at every step |
| Involved lenses | HUMAN-DIRECTOR (deployment authority), TRUTH-Q (pre/post state verification), SAFE-Q (live monitoring), SECURE-Q (artifact integrity), RECORDS-Q (deployment record) |
| Kernel services | `core/audit.py`, `core/charter_kernel.py`, `core/scheduler.py`, `core/buddy_protocol.py` |
| Key axioms | No action without audit; Rest and protection are structural; Immutable Charter Kernel outranks everything |
| Inputs | Approved Change Record from P06; deployment environment specification; rollback plan |
| Outputs | Deployment record in `data/changes/deployed/`; `DEPLOYMENT_COMPLETE` or `ROLLBACK_EXECUTED` AuditEvent |

---

## Pre-deployment checklist

Before any deployment step executes, all of the following must be confirmed:

- [ ] Approved Change Record exists and `CHANGE_APPROVED` AuditEvent is present.
- [ ] Rollback plan is documented and verified (not just described).
- [ ] SAFE-Q has confirmed monitoring is in place for the target environment.
- [ ] Sabbath status is checked; deployment during Sabbath requires HUMAN-DIRECTOR explicit declaration.
- [ ] Charter integrity verified by `core/charter_kernel.py`.

---

## Flow

1. **Pre-deployment snapshot**
   - RECORDS-Q captures a snapshot of the pre-change state (system version, configuration hashes).
   - Stored in `archive/changes/snapshots/` with AuditEvent `PRE_DEPLOYMENT_SNAPSHOT`.

2. **Controlled execution**
   - Changes are executed in steps; each step emits a `DEPLOYMENT_STEP` AuditEvent.
   - SAFE-Q monitors for anomalies throughout; any anomaly triggers an immediate pause.

3. **Post-change verification**
   - TRUTH-Q verifies that the post-change state matches the expected specification.
   - SECURE-Q verifies artifact integrity (checksums, signatures).
   - If verification fails → automatic rollback trigger.

4. **Rollback path**
   - Rollback is triggered by: SAFE-Q anomaly flag, TRUTH-Q verification failure, HUMAN-DIRECTOR decision, or any lens emitting `ROLLBACK_REQUESTED`.
   - Rollback steps are executed in reverse order using the pre-deployment snapshot.
   - AuditEvent `ROLLBACK_EXECUTED` is emitted with reason and executing lens.
   - A rollback is never treated as a failure to be hidden; it is a constitutional success (protection worked).

5. **Deployment close**
   - Successful deployment: HUMAN-DIRECTOR emits `DEPLOYMENT_COMPLETE`.
   - Deployment record is sealed in `data/changes/deployed/`.
   - Pattern P08 (Retrospective) is automatically scheduled.

---

## Related files

- `src/safety/deployment.py` – implementation.
- `config/safety_policy.yaml` – monitoring parameters, rollback timeout thresholds.
