# Pattern P04 – Regulatory Reporting

## Template fields

| Field | Value |
|---|---|
| Name | Regulatory Reporting |
| Domain / primary axis | Accounting · Truth · Power |
| Intent | Assemble, validate, and certify reports for regulatory submission with a complete, immutable audit trail |
| Involved lenses | TRUTH-Q (data completeness and accuracy), AUDIT-Q (regulatory alignment), RISK-Q (disclosure adequacy), RECORDS-Q (version and packaging), HUMAN-DIRECTOR (certification and sign-off) |
| Kernel services | `core/audit.py`, `core/charter_kernel.py`, `core/reflection.py`, `core/scheduler.py` |
| Key axioms | No action without audit; Immutable Charter Kernel outranks everything; Rest and protection are structural |
| Inputs | Finalized reconciled ledgers, approved adjustments, prior-period reports, policy configuration |
| Outputs | Signed regulatory report package in `archive/reports/YYYY-QN/`; submission AuditEvent chain |

---

## Flow

1. **Pre-assembly checklist**
   - AUDIT-Q confirms that all required P01 ingestions, P02 reconciliations, and P03 adjustments
     for the reporting period are complete and acknowledged.
   - Any open items block the assembly step and notify HUMAN-DIRECTOR.

2. **Report assembly**
   - TRUTH-Q aggregates data from finalized ledgers and adjustments into the report structure.
   - RECORDS-Q assigns a version ID and writes the draft to `data/reports/regulatory/draft/`.

3. **Pre-reflection pause**
   - If a reflection window is due, work pauses and EVAL-Q schedules a review session
     before any submission package is sealed.

4. **Multi-lens review**
   - TRUTH-Q checks completeness and arithmetic accuracy.
   - AUDIT-Q checks regulatory framework alignment (applicable standards are listed in `config/accounting_policy.yaml`).
   - RISK-Q checks that all material items are disclosed.
   - Each lens emits a `REPORT_REVIEWED` AuditEvent with a status field.

5. **Charter integrity gate**
   - `core/charter_kernel.py` is called once more before final certification.

6. **Certification and sealing**
   - HUMAN-DIRECTOR reviews the report and all review AuditEvents.
   - On approval, emits `REPORT_CERTIFIED` with a signature reference.
   - RECORDS-Q seals the package into `archive/reports/YYYY-QN/` as an immutable snapshot.
   - Submission metadata (timestamps, regulatory body, reference IDs) are logged.

7. **Post-submission reflection**
   - After submission, EVAL-Q schedules a short retrospective:
     - Were variances material or trivial?
     - Did any pattern perform unexpectedly?
     - What should be refined before the next period?
   - Findings are written to `archive/stories/` as a narrative AuditEvent.

---

## Related files

- `src/accounting/reporting.py` – implementation.
- `config/accounting_policy.yaml` – regulatory framework identifiers, materiality thresholds.
- `archive/reports/` – sealed report packages by period.
