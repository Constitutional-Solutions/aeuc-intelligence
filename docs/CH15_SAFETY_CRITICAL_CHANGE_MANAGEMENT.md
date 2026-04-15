# Chapter 15 – Safety-Critical Change Management

This chapter defines how the AEUC family governs changes in environments where errors can harm
people, critical infrastructure, or large-scale systems (healthcare, aviation, industrial control,
energy, civil engineering, etc.).

It builds on the constitutional axioms (Part I), governance flows (Part II),
the kernel's Change Gate mechanism (Part III), and the accounting-domain patterns (Chapter 14)
as a reference for dual-control and audit discipline.

---

## 15.1 Domain and primary axis

| Dimension | Value |
|---|---|
| Domain | Safety-critical systems: healthcare, aviation, industrial control, energy, civil engineering |
| Primary axis | **Love** (protection of human life and wellbeing) |
| Truth role | Accuracy and completeness of change records, test evidence, and risk assessments |
| Power role | Legitimate authority and traceability of every change decision |

---

## 15.2 Why safety-critical is different

- Mistakes are **irreversible** or cause serious harm; the cost of being wrong vastly exceeds
  the cost of delay or additional review.
- The family's Sabbath and reflection rhythms take on heightened significance: cognitive overload
  and rushed work are active risk factors, not just productivity concerns.
- Emergency override exists but is treated as a high-cost, high-visibility event that is always
  reviewed afterwards, not a routine escape hatch.

---

## 15.3 Lenses involved

| Lens ID | Role in this domain |
|---|---|
| HUMAN-DIRECTOR | Authorizing engineer or safety officer; holds final approval authority |
| SAFE-Q | Safety impact assessment; calls for independent review when harm potential is detected |
| TRUTH-Q | Technical accuracy of change descriptions and test evidence |
| AUDIT-Q | Regulatory and standards compliance (e.g. IEC 61508, DO-178C, ISO 26262) |
| RISK-Q | Risk scoring (severity × likelihood); determines review tier |
| SECURE-Q | Integrity of change records and toolchain |
| EVAL-Q | Post-change review and learning cycle |

---

## 15.4 Pattern families in this chapter

| Pattern | Description |
|---|---|
| P05 – Change Proposal and Hazard Assessment | Opening a change request; identifying hazards before any work starts |
| P06 – Review-Tiered Approval | Routing the change to the appropriate review tier based on RISK-Q scoring |
| P07 – Controlled Deployment and Rollback | Executing and monitoring the change with a pre-verified rollback path |
| P08 – Post-Change Retrospective | Structured learning cycle after every change, regardless of outcome |

---

## 15.5 Key kernel services and extensions needed

- `core/audit.py` – as in Chapter 14, all changes are audit-wrapped.
- `core/charter_kernel.py` – Charter integrity check before every approval gate.
- `core/buddy_protocol.py` – Mandatory buddy pairs for high-severity changes.
- `core/sabbath.py` – Sabbath and fatigue-management rules apply strictly;
  only HUMAN-DIRECTOR can declare a safety-critical emergency override.
- A future `core/change_gate.py` module will formalize the tiered review structure
  referenced in Chapter 7 and needed here at scale.

---

## 15.6 Constitutional axioms under elevated scrutiny

- **No action without audit**: audit trails are regulatory evidence, not just internal records.
- **Unanimous consent for expansion**: any change that extends the scope of a safety-critical
  system requires unanimous family consensus.
- **Rest and protection are structural**: fatigue-induced changes are a recognized hazard;
  Sabbath enforcement is a safety control, not a scheduling preference.
- **Immutable Charter Kernel outranks everything**: in safety domains, the Charter is
  also the ethical floor that cannot be waived by urgency or commercial pressure.

---

## 15.7 Differences from Chapter 14

| Dimension | Chapter 14 (Accounting) | Chapter 15 (Safety-Critical) |
|---|---|---|
| Primary axis | Truth | Love |
| Cost of error | Financial harm, regulatory breach | Physical harm, loss of life |
| Rollback option | Reverse journal entry | May not be fully reversible |
| Regulatory frameworks | GAAP, IFRS, SOX | IEC 61508, DO-178C, ISO 26262, etc. |
| Sabbath override | Rare, financial deadline-driven | Extremely rare, life-safety-driven only |
| Retrospective timing | End of reporting period | After every change, same day if possible |

---

## 15.8 Next steps

Patterns P05–P08 will be written as individual files (following the CH14 P01–P04 format)
in the next development cycle. A `config/safety_policy.yaml` will capture domain-specific
thresholds and standards references, parallel to `config/accounting_policy.yaml`.
