# Pattern P12 – Model Monitoring and Drift Response

## Template fields

| Field | Value |
|---|---|
| Name | Model Monitoring and Drift Response |
| Domain / primary axis | Learning & Model Governance · Truth · Love |
| Intent | Continuously monitor production models for performance degradation, distributional drift, and harmful output patterns; respond constitutionally when thresholds are breached |
| Involved lenses | TRUTH-Q (performance metrics), SAFE-Q (harmful output detection), RISK-Q (drift severity scoring), EVAL-Q (triggered re-evaluation), HUMAN-DIRECTOR (response authority) |
| Kernel services | `core/audit.py`, `core/scheduler.py`, `core/reflection.py`, `core/sabbath.py` |
| Key axioms | No action without audit; Rest and protection are structural |
| Inputs | Live model inference logs, ground-truth feedback (where available), drift detection metrics |
| Outputs | Monitoring reports in `data/reports/model_monitoring/`; `DRIFT_DETECTED` or `MODEL_SUSPENDED` AuditEvents |

---

## Flow

1. **Scheduled monitoring runs**
   - `core/scheduler.py` triggers monitoring tasks at intervals defined in `config/model_policy.yaml` → `monitoring_interval_hours`.
   - Sabbath windows are respected; monitoring continues in read-only mode during Sabbath (no response actions).

2. **Metric collection (TRUTH-Q)**
   - Performance metrics (accuracy, precision, recall, calibration error) are computed on available feedback.
   - Distribution metrics (feature drift, output distribution shift) are computed.
   - Results logged as `MONITORING_RUN` AuditEvent.

3. **Harmful output scan (SAFE-Q)**
   - SAFE-Q reviews a sample of model outputs for harmful or biased patterns.
   - Any flagged output triggers an immediate `HARMFUL_OUTPUT_DETECTED` AuditEvent.

4. **Drift severity scoring (RISK-Q)**
   - RISK-Q scores detected drift by severity and urgency.
   - Tiers:
     - Low: log and monitor more frequently.
     - Medium: trigger EVAL-Q re-evaluation.
     - High: suspend model and notify HUMAN-DIRECTOR.

5. **Response actions**
   - Low drift: increase monitoring frequency; log.
   - Medium drift: EVAL-Q runs P11 re-evaluation; model stays live pending results.
   - High drift or harmful output: SAFE-Q or RISK-Q emits `MODEL_SUSPENDED`; model is pulled from production pending HUMAN-DIRECTOR decision.

6. **Reflection integration**
   - At each Sabbath-aligned reflection window, EVAL-Q reviews cumulative drift trends.
   - Findings feed back into the next training/experiment cycle (P10).

---

## Related files

- `src/models/monitoring.py` – implementation.
- `config/model_policy.yaml` – monitoring intervals, drift thresholds, harmful output categories.
