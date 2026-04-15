# Pattern P11 – Model Evaluation and Promotion Gate

## Template fields

| Field | Value |
|---|---|
| Name | Model Evaluation and Promotion Gate |
| Domain / primary axis | Learning & Model Governance · Truth · Power |
| Intent | Ensure no model enters production without a complete, independent evaluation, a passing risk score, and explicit HUMAN-DIRECTOR authorization |
| Involved lenses | TRUTH-Q (accuracy, calibration, failure modes), EVAL-Q (independent evaluation), RISK-Q (bias, safety, regulatory exposure), AUDIT-Q (data governance and compliance), SECURE-Q (artifact integrity), HUMAN-DIRECTOR (final sign-off) |
| Kernel services | `core/audit.py`, `core/charter_kernel.py`, `core/buddy_protocol.py` |
| Key axioms | No action without audit; Unanimous consent for expansion; Immutable Charter Kernel outranks everything |
| Inputs | Candidate model artifacts (weights, config, training run AuditEvents), P10 experiment record |
| Outputs | Promotion record in `data/models/production/`; `MODEL_PROMOTED` or `MODEL_REJECTED` AuditEvent |

---

## Flow

1. **Promotion request**
   - EXPLORE-Q or HUMAN-DIRECTOR submits a promotion request referencing the P10 experiment record.
   - AuditEvent `PROMOTION_REQUESTED` is emitted.

2. **Charter integrity check**
   - `core/charter_kernel.py` verifies integrity before evaluation begins.

3. **Artifact integrity (SECURE-Q)**
   - Model weights and configuration files are hash-verified against the experiment record.
   - Any hash mismatch blocks promotion.

4. **Independent evaluation (EVAL-Q + TRUTH-Q)**
   - EVAL-Q runs evaluation independently of EXPLORE-Q (no access to EXPLORE-Q's internal notes).
   - TRUTH-Q checks accuracy, calibration, and known failure modes on a held-out evaluation set.
   - Buddy protocol: EVAL-Q and TRUTH-Q are paired; neither can approve alone.

5. **Risk scoring (RISK-Q)**
   - RISK-Q scores the model for bias, safety risks, and regulatory exposure.
   - Score must be below `model_policy.yaml` → `promotion_risk_threshold` for promotion to proceed.

6. **Compliance review (AUDIT-Q)**
   - AUDIT-Q confirms all datasets used in training are approved for production use.
   - Any research-only dataset in the training lineage blocks promotion.

7. **HUMAN-DIRECTOR sign-off**
   - HUMAN-DIRECTOR reviews all evaluation and risk reports.
   - Emits `MODEL_PROMOTED` (approval) or `MODEL_REJECTED` (rejection with reason).

8. **Promotion**
   - Approved model artifacts are copied to `data/models/production/` with immutable provenance.
   - Pattern P12 (monitoring) is automatically activated.

---

## Related files

- `src/models/promotion.py` – implementation.
- `config/model_policy.yaml` – risk thresholds, evaluation requirements.
