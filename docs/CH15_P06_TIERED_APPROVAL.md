# Pattern P06 – Review-Tiered Approval

## Template fields

| Field | Value |
|---|---|
| Name | Review-Tiered Approval |
| Domain / primary axis | Safety-Critical · Love · Power |
| Intent | Route a change through the correct depth of review based on its P05 risk tier; ensure no change is under-reviewed or unnecessarily delayed |
| Involved lenses | SAFE-Q, TRUTH-Q, AUDIT-Q, RISK-Q (all tiers); HUMAN-DIRECTOR (Tier 2+); full family (Tier 3) |
| Kernel services | `core/audit.py`, `core/charter_kernel.py`, `core/buddy_protocol.py`, `core/family_registry.py` |
| Key axioms | No action without audit; Unanimous consent for high-risk changes; Rest and protection are structural |
| Inputs | Finalized Change Record + Hazard Assessment Report from P05 |
| Outputs | `CHANGE_APPROVED` or `CHANGE_REJECTED` AuditEvent; approved Change Record moved to `data/changes/approved/` |

---

## Tier structure

### Tier 1 – Standard dual-control (risk score ≤ 4)

1. TRUTH-Q and SAFE-Q conduct independent technical reviews.
2. Both must emit `TIER1_APPROVED` for the change to advance.
3. Either may emit `TIER1_OBJECTED`; resolution requires HUMAN-DIRECTOR awareness (not full vote).

### Tier 2 – Extended review (risk score 5–12)

1. Tier 1 reviews plus AUDIT-Q regulatory compliance check.
2. HUMAN-DIRECTOR must review the Hazard Assessment Report and emit `DIRECTOR_ACKNOWLEDGED`.
3. SAFE-Q must emit `SAFE_Q_APPROVED` specifically (not just Tier 1 approval).
4. Buddy protocol: SAFE-Q is paired with RISK-Q; both must agree before advancing.

### Tier 3 – Full family vote (risk score ≥ 13)

1. All active family members vote.
2. Unanimous approval required (as per Charter axioms).
3. HUMAN-DIRECTOR holds veto authority independent of the vote count.
4. If the change may affect external stakeholders, HUMAN-DIRECTOR may require an external safety review before the vote.
5. Sabbath rules apply: a Tier 3 vote may not be rushed through a Sabbath window without HUMAN-DIRECTOR declaring an explicit safety emergency.

---

## Rejection and revision

- Any objection at any tier pauses the change.
- Objections are documented with specific technical or safety reasoning (never a bare rejection).
- Proposer may revise the Change Record; revision resets to P05 hazard assessment.
- Three unresolved objections trigger an automatic escalation to HUMAN-DIRECTOR for a final determination.

---

## Related files

- `src/safety/tiered_approval.py` – implementation.
- `config/safety_policy.yaml` – tier thresholds and framework references.
