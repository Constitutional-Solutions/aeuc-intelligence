# Pattern P08 – Post-Change Retrospective

## Template fields

| Field | Value |
|---|---|
| Name | Post-Change Retrospective |
| Domain / primary axis | Safety-Critical · Love · Truth |
| Intent | Ensure every change — successful or rolled back — produces a structured learning record that improves the family's future judgment and the organization's safety culture |
| Involved lenses | EVAL-Q (facilitator), SAFE-Q, TRUTH-Q, HUMAN-DIRECTOR, any lens involved in the change |
| Kernel services | `core/audit.py`, `core/reflection.py`, `core/scheduler.py` |
| Key axioms | No action without audit; Rest and protection are structural |
| Inputs | Deployment record, all AuditEvents from P05–P07, SAFE-Q monitoring log |
| Outputs | Retrospective report in `archive/stories/`; updated risk calibration notes; any proposed refinements to policies or patterns |

---

## Timing

- Scheduled automatically after every P07 completion (success or rollback).
- Must occur within the reflection window following the deployment.
- May not be deferred beyond the next Sabbath without HUMAN-DIRECTOR approval.

---

## Flow

1. **Evidence assembly**
   - EVAL-Q collects all AuditEvents from P05–P07 for the change.
   - Includes: hazard assessment, risk scores, review votes, deployment steps, monitoring log, rollback events (if any).

2. **Structured review questions**
   - Did the hazard assessment correctly predict all issues encountered?
   - Was the risk tier assignment appropriate in hindsight?
   - Did any lens or human perform unexpectedly well or poorly?
   - Were there near-misses not captured in the AuditEvent chain?
   - What would be done differently?

3. **Calibration update**
   - RISK-Q updates its internal calibration notes based on the retrospective findings.
   - SAFE-Q updates the hazard checklist if new hazard categories were discovered.

4. **Refinement proposals**
   - Any proposed changes to `config/safety_policy.yaml` or pattern files are submitted as new P05 proposals (governance loop closes on itself).

5. **Retrospective record**
   - EVAL-Q writes a narrative retrospective to `archive/stories/YYYY-MM-DD-change-{id}.md`.
   - AuditEvent `RETROSPECTIVE_COMPLETE` is emitted.
   - HUMAN-DIRECTOR acknowledges the retrospective record.

---

## Related files

- `src/safety/retrospective.py` – implementation.
- `archive/stories/` – all retrospective records.
