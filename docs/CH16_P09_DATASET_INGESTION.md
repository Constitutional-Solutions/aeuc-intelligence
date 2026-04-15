# Pattern P09 – Dataset Ingestion and Provenance

## Template fields

| Field | Value |
|---|---|
| Name | Dataset Ingestion and Provenance |
| Domain / primary axis | Learning & Model Governance · Truth |
| Intent | Bring datasets into the research or production environment with complete lineage, integrity verification, and constitutional tagging (research vs production) |
| Involved lenses | RECORDS-Q (steward), TRUTH-Q (schema and quality), SECURE-Q (integrity), AUDIT-Q (privacy and data governance compliance), HUMAN-DIRECTOR (approval of new data sources) |
| Kernel services | `core/audit.py`, `core/charter_kernel.py`, `core/scheduler.py` |
| Key axioms | No action without audit; Research and production separation |
| Inputs | Raw datasets from external sources, partner systems, or internal collection |
| Outputs | Tagged, normalized datasets in `data/datasets/research/` or `data/datasets/production/`; AuditEvent `DATASET_INGESTED` |

---

## Flow

1. **Source registration**
   - All new data sources must be registered in `config/model_policy.yaml` → `approved_data_sources` before ingestion.
   - Unregistered sources require HUMAN-DIRECTOR approval (governance gate).

2. **Integrity and privacy scan**
   - SECURE-Q hashes the raw dataset and logs the hash.
   - AUDIT-Q scans for PII and data governance obligations; any finding blocks ingestion until resolved.

3. **Schema and quality check (TRUTH-Q)**
   - Schema is validated against a registered schema definition.
   - Quality metrics (completeness, value distributions, anomaly flags) are computed and logged.

4. **Constitutional tagging**
   - Dataset is tagged: `env: research` or `env: production`.
   - Research datasets may not be used in production model training without promotion (see P11).
   - AuditEvent `DATASET_INGESTED` includes tag, source hash, quality metrics, and lens IDs.

5. **Archive raw**
   - Raw dataset is archived to `archive/datasets/raw/` as immutable.
   - Processed/normalized version goes to `data/datasets/{env}/`.

---

## Related files

- `src/models/dataset_ingestion.py` – implementation.
- `config/model_policy.yaml` – approved data sources, PII policy, schema registry.
