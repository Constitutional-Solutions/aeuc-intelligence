# Chapter 14 – Accounting and Records Stewardship

This chapter fully defines how the AEUC family supports an accounting firm or records team.
Every pattern here is constitutional: traceable to Charter axioms, enforced by kernel services,
and governed by family lenses that are responsible to Love · Truth · Power.

---

## 14.1 Domain and primary axis

| Dimension | Value |
|---|---|
| Domain | Financial accounting, auditing, records management |
| Primary axis | **Truth** |
| Love role | Protecting clients, staff, and counterparties from harm |
| Power role | Ensuring decisions made from records are legitimate and auditable |

The Truth axis means that this domain treats correctness and completeness of records as a
constitutional duty — not just a professional standard. Errors are not merely inconveniences;
they are violations of the family's constitutional obligation to reality.

---

## 14.2 Lenses involved

| Lens ID | Role in this domain |
|---|---|
| HUMAN-DIRECTOR | Partner / lead accountant; the ultimate decision-maker and conscience |
| TRUTH-Q | Consistency checking, reconciliation, anomaly detection |
| AUDIT-Q | Sampling, evidence chains, regulatory alignment |
| RISK-Q | Materiality and impact assessment of discrepancies |
| RECORDS-Q | File, ledger, and version stewardship |
| SECURE-Q | Access control, confidentiality, tamper detection |
| EVAL-Q | Quality assessment and reflection scoring for finished work |

All seven lenses are defined in the family registry. See `config/family_registry.yaml` and
`docs/FAMILY_MEMBER_INDEX.md` for full LensSpec details.

---

## 14.3 Kernel services used

| Kernel service | How it is used here |
|---|---|
| `core/audit.py` | Wraps every ledger write, adjustment, and report generation as an AuditEvent |
| `core/scheduler.py` | Queues ingestion, reconciliation, and report tasks; respects Sabbath |
| `core/sabbath.py` | Enforces rest periods; no batch work during Sabbath unless declared emergency |
| `core/reflection.py` | Schedules weekly reconciliation reviews aligned with reflection windows |
| `core/buddy_protocol.py` | Pairs TRUTH-Q with AUDIT-Q and RISK-Q for dual-control on sensitive adjustments |
| `core/family_registry.py` | Resolves lens IDs and status before any task is dispatched |
| `core/charter_kernel.py` | Validates Charter integrity before high-risk operations |

---

## 14.4 Patterns in this chapter

| Pattern | File |
|---|---|
| P01 – Ledger Ingestion and Normalization | `docs/CH14_P01_LEDGER_INGESTION.md` |
| P02 – Reconciliation and Variance Analysis | `docs/CH14_P02_RECONCILIATION.md` |
| P03 – Change-Controlled Adjustment | `docs/CH14_P03_ADJUSTMENT.md` |
| P04 – Regulatory Reporting | `docs/CH14_P04_REGULATORY_REPORTING.md` |

---

## 14.5 Constitutional axioms enforced

- **No action without audit**: every ledger transformation is logged.
- **No member without spec and tests**: all lenses in this domain have LensSpecs with test plans.
- **Unanimous consent for high-risk changes**: material adjustments require all active lenses to vote.
- **Research and production separation**: experimental analysis scripts live in `src/research/`;
  production ledger operations live in `src/accounting/`.
- **Rest and protection are structural**: Sabbath windows are respected; lenses have buddies for support.
- **Immutable Charter Kernel outranks everything**: Charter integrity is verified before any
  period-closing or regulatory submission.

---

## 14.6 Supporting scripts and modules

- `src/accounting/helpers.py` – shared utility functions for ledger parsing and normalization.
- `src/accounting/ingestion.py` – Ledger ingestion script (Pattern P01).
- `src/accounting/reconciliation.py` – Reconciliation engine (Pattern P02).
- `src/accounting/adjustment.py` – Dual-control adjustment workflow (Pattern P03).
- `src/accounting/reporting.py` – Regulatory report assembler (Pattern P04).

---

## 14.7 Data and file conventions

- **Raw inputs** are always stored in `data/raw/` and treated as immutable once received.
- **Normalized outputs** go to `data/processed/`.
- **Period snapshots** go to `archive/ledgers/YYYY-MM/`.
- All files include a provenance header comment or metadata block identifying:
  - Source system and export date.
  - Ingestor (lens ID or human name).
  - Audit event ID for the ingestion run.
