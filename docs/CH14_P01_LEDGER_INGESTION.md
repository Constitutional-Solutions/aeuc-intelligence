# Pattern P01 – Ledger Ingestion and Normalization

## Template fields

| Field | Value |
|---|---|
| Name | Ledger Ingestion and Normalization |
| Domain / primary axis | Accounting · Truth |
| Intent | Bring raw ledger exports into the system in a provenance-preserving, immutable way; normalize them to a canonical format before any analysis |
| Involved lenses | RECORDS-Q (steward), TRUTH-Q (format and schema validation), SECURE-Q (access and integrity), HUMAN-DIRECTOR (approval of new source types) |
| Kernel services | `core/audit.py`, `core/scheduler.py`, `core/charter_kernel.py` |
| Key axioms | No action without audit; Research and production separation |
| Inputs | Raw CSV, XLSX, JSON, or ERP exports from source systems |
| Outputs | Canonical normalized ledger files in `data/processed/`; AuditEvent per ingestion run |

---

## Flow

1. **Receive raw file**
   - File is dropped into `data/raw/` by a human or an automated connector.
   - RECORDS-Q logs the arrival as an AuditEvent (`RECORDS_RAW_RECEIVED`).

2. **Schema detection and validation**
   - TRUTH-Q reads the file and determines its schema (source system, column layout, currency/date conventions).
   - If schema is unknown, a governance gate opens: HUMAN-DIRECTOR must approve the new format before processing continues.

3. **Normalization**
   - Columns are mapped to the canonical ledger schema (see `src/accounting/helpers.py` → `CANONICAL_COLUMNS`).
   - Date formats are standardized to ISO-8601.
   - Amounts are normalized to the reporting currency with exchange rate metadata preserved.
   - A provenance block is written to each output file.

4. **Integrity check**
   - Row counts and control totals from the raw file are compared to the normalized output.
   - Any discrepancy is logged as an AuditEvent (`INGESTION_INTEGRITY_MISMATCH`) and queued for TRUTH-Q review before downstream use.

5. **Archive raw file**
   - Raw file is moved to `archive/ledgers/raw/YYYY-MM/` and marked immutable.
   - AuditEvent `INGESTION_COMPLETE` is emitted with source hash, row counts, and output file path.

---

## Error handling

- Schema mismatch → open governance gate.
- Integrity mismatch → pause downstream; queue TRUTH-Q review.
- Corrupted file → emit `INGESTION_FAILED`; notify HUMAN-DIRECTOR.

---

## Related files

- `src/accounting/ingestion.py` – implementation of this pattern.
- `src/accounting/helpers.py` – canonical schema and shared utilities.
