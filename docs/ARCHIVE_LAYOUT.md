# Archive Layout

This document defines the canonical directory structure for the `archive/` tree.
All modules and patterns must use these paths rather than creating ad-hoc directories.

```
archive/
  ledgers/
    raw/
      YYYY-MM/        # Immutable raw ledger exports, organized by period
    processed/
      YYYY-MM/        # Canonical normalized ledger files
  adjustments/
    YYYY-MM/          # Approved and posted adjustment records
  reports/
    regulatory/
      YYYY-QN/        # Sealed regulatory report packages (e.g. 2026-Q1)
    reconciliation/
      YYYY-MM/        # Reconciliation variance reports
  logs/
    audit/            # Append-only AuditEvent log files
    scheduler/        # Scheduler dispatch logs
  registry/
    snapshots/        # Point-in-time snapshots of family_registry.yaml
  stories/
                      # Narrative AuditEvents and retrospective notes
```

## Rules

- Directories under `archive/ledgers/raw/` are **write-once** after initial ingestion.
- Sealed report packages under `archive/reports/regulatory/` may not be modified after
  `REPORT_CERTIFIED` is emitted.
- Log files under `archive/logs/audit/` are **append-only**.
- Any module creating a new archive subdirectory must document it here first.
