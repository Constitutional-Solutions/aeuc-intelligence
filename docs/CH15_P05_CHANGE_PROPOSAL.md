# Pattern P05 – Change Proposal and Hazard Assessment

## Template fields

| Field | Value |
|---|---|
| Name | Change Proposal and Hazard Assessment |
| Domain / primary axis | Safety-Critical · Love |
| Intent | Open a change request with a structured hazard assessment before any work begins; ensure no change enters the approval pipeline without a documented risk profile |
| Involved lenses | HUMAN-DIRECTOR (proposer or sponsor), SAFE-Q (hazard identification), RISK-Q (severity × likelihood scoring), TRUTH-Q (technical accuracy of proposal), AUDIT-Q (regulatory framework mapping) |
| Kernel services | `core/audit.py`, `core/charter_kernel.py`, `core/family_registry.py` |
| Key axioms | No action without audit; Unanimous consent for expansion; Immutable Charter Kernel outranks everything |
| Inputs | Change description, affected systems/components, proposed approach, supporting evidence references |
| Outputs | Numbered Change Record in `data/changes/proposed/`; Hazard Assessment Report; AuditEvent `CHANGE_PROPOSED` |

---

## Flow

1. **Proposal submission**
   - Proposer (human or lens) submits a Change Record including:
     - Unique change ID (auto-assigned).
     - Affected systems and components (with version references).
     - Narrative description of the change and its intent.
     - At least one supporting evidence reference (test plan, specification, safety case).
   - AuditEvent `CHANGE_PROPOSED` is emitted immediately.

2. **Charter integrity check**
   - `core/charter_kernel.py` verifies the Charter hash.
   - If Charter integrity fails, the proposal is quarantined until HUMAN-DIRECTOR resolves the discrepancy.

3. **Hazard identification (SAFE-Q)**
   - SAFE-Q reviews the affected systems and identifies potential hazards using the checklist in `config/safety_policy.yaml` → `hazard_categories`.
   - Each hazard is assigned a category (e.g. `PHYSICAL_HARM`, `DATA_CORRUPTION`, `SERVICE_INTERRUPTION`, `REGULATORY_BREACH`).
   - AuditEvent `HAZARD_IDENTIFIED` is emitted per hazard.

4. **Risk scoring (RISK-Q)**
   - RISK-Q scores each hazard: severity (1–5) × likelihood (1–5) = risk score.
   - Scores determine the review tier (see Pattern P06):
     - Score ≤ 4: Tier 1 (standard dual-control).
     - Score 5–12: Tier 2 (extended review, requires SAFE-Q sign-off).
     - Score ≥ 13: Tier 3 (full family vote + HUMAN-DIRECTOR; may require external safety review).
   - AuditEvent `RISK_SCORED` is emitted with scores and tier assignment.

5. **Technical accuracy check (TRUTH-Q)**
   - TRUTH-Q verifies the technical description is accurate and complete.
   - Any inaccuracies are returned to the proposer for correction before the proposal advances.

6. **Regulatory mapping (AUDIT-Q)**
   - AUDIT-Q maps the change to applicable standards listed in `config/safety_policy.yaml` → `regulatory_frameworks`.
   - Identifies any compliance obligations triggered by the change.

7. **Proposal finalization**
   - Hazard Assessment Report is written to `data/changes/proposed/`.
   - Proposal advances to Pattern P06 for tiered approval.

---

## Error handling

- Charter integrity failure → quarantine; notify HUMAN-DIRECTOR.
- Incomplete proposal (missing evidence reference) → returned to proposer; not quarantined.
- TRUTH-Q accuracy objection → revision required before advancing.

---

## Related files

- `src/safety/change_proposal.py` – implementation.
- `config/safety_policy.yaml` – hazard categories, risk thresholds, regulatory frameworks.
