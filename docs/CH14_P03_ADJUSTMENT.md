# Pattern P03 – Change-Controlled Adjustment

## Template fields

| Field | Value |
|---|---|
| Name | Change-Controlled Adjustment |
| Domain / primary axis | Accounting · Truth · Power |
| Intent | Allow corrective or reclassification journal entries to be posted only through an explicit, dual-control, constitutionally-governed process |
| Involved lenses | HUMAN-DIRECTOR (proposer or final approver), TRUTH-Q (impact check), AUDIT-Q (evidence review), RISK-Q (materiality gate), SECURE-Q (tamper detection) |
| Kernel services | `core/audit.py`, `core/charter_kernel.py`, `core/buddy_protocol.py`, `core/family_registry.py` |
| Key axioms | No action without audit; Unanimous consent for material changes; Immutable Charter Kernel outranks everything |
| Inputs | Adjustment proposal (lens ID or human, amount, accounts, reason, supporting evidence reference) |
| Outputs | Posted journal entry in `data/processed/adjustments/`; full governance AuditEvent chain |

---

## Flow

1. **Proposal**
   - Any active lens or HUMAN-DIRECTOR may propose an adjustment.
   - Proposal must include: affected accounts, amount, narrative reason, and at least one evidence reference.
   - AuditEvent `ADJUSTMENT_PROPOSED` is emitted.

2. **Charter integrity check**
   - `core/charter_kernel.py` is called to verify Charter hash before any vote opens.
   - If Charter hash fails, the entire adjustment process halts and HUMAN-DIRECTOR is notified.

3. **Materiality gate**
   - RISK-Q scores the proposed adjustment.
   - If materiality is above threshold (defined in `config/accounting_policy.yaml`), a full family vote is required.
   - Below threshold: TRUTH-Q and AUDIT-Q co-approval is sufficient.

4. **Dual-control review**
   - TRUTH-Q checks that the adjustment is arithmetically correct and consistent with the underlying ledger.
   - AUDIT-Q reviews the evidence chain and regulatory compliance.
   - SECURE-Q verifies that no tampered files are in the evidence set.
   - Each lens emits its vote AuditEvent: `ADJUSTMENT_APPROVED` or `ADJUSTMENT_OBJECTED`.

5. **Posting**
   - If all required votes are `APPROVED`, the adjustment is posted as a new record in
     `data/processed/adjustments/` (never overwriting originals).
   - AuditEvent `ADJUSTMENT_POSTED` is emitted with full vote chain and posting timestamp.

6. **Objection handling**
   - Any `ADJUSTMENT_OBJECTED` vote pauses the process.
   - HUMAN-DIRECTOR reviews the objection and may either revise the proposal or escalate to an
     emergency governance session.
   - Unresolved objections are never silently overridden.

---

## Related files

- `src/accounting/adjustment.py` – implementation.
- `config/accounting_policy.yaml` – materiality thresholds and policy parameters.
