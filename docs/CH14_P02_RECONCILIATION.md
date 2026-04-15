# Pattern P02 – Reconciliation and Variance Analysis

## Template fields

| Field | Value |
|---|---|
| Name | Reconciliation and Variance Analysis |
| Domain / primary axis | Accounting · Truth |
| Intent | Compare two or more normalized ledgers (or internal vs external statements) and surface all variances for human review |
| Involved lenses | TRUTH-Q (primary), AUDIT-Q (evidence tagging), RISK-Q (materiality scoring), HUMAN-DIRECTOR (review and sign-off) |
| Kernel services | `core/audit.py`, `core/scheduler.py`, `core/reflection.py`, `core/buddy_protocol.py` |
| Key axioms | No action without audit; Unanimous consent for material adjustments |
| Inputs | Two or more canonical ledger files from `data/processed/` |
| Outputs | Variance report in `data/reports/reconciliation/`; AuditEvents per matched and unmatched item |

---

## Flow

1. **Define reconciliation scope**
   - HUMAN-DIRECTOR (or a delegated lens) specifies which ledgers to reconcile and the matching key (e.g., transaction ID, date range, account code).

2. **Matching pass**
   - TRUTH-Q reads both ledgers and attempts exact matches on the matching key.
   - Matched items are stamped with `RECON_MATCHED` AuditEvents.
   - Unmatched items enter the variance queue.

3. **Variance classification**
   - RISK-Q scores each variance by materiality (amount, affected accounts, regulatory significance).
   - AUDIT-Q tags each variance with the relevant regulatory or policy reference (if known).
   - Classifications: `TIMING_DIFFERENCE`, `KNOWN_ADJUSTMENT`, `UNEXPLAINED_VARIANCE`, `POSSIBLE_ERROR`.

4. **Reflection pause**
   - Before the report is finalized, the scheduler checks whether a reflection window is due.
   - If yes, work is paused and EVAL-Q schedules a review session with TRUTH-Q and HUMAN-DIRECTOR.

5. **Report generation**
   - A structured variance report is written to `data/reports/reconciliation/`.
   - HUMAN-DIRECTOR must acknowledge the report (AuditEvent `RECON_ACKNOWLEDGED`) before downstream patterns (P03, P04) can use it.

---

## Buddy protocol

TRUTH-Q is buddied with AUDIT-Q during this pattern. If TRUTH-Q flags an item as `POSSIBLE_ERROR`,
AUDIT-Q independently reviews the evidence chain before RISK-Q scores it.
Neither lens can clear a `POSSIBLE_ERROR` alone.

---

## Related files

- `src/accounting/reconciliation.py` – implementation.
- `src/accounting/helpers.py` – shared utilities.
