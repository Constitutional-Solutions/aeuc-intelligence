# Pattern P10 – Experiment Lifecycle

## Template fields

| Field | Value |
|---|---|
| Name | Experiment Lifecycle |
| Domain / primary axis | Learning & Model Governance · Truth |
| Intent | Define, run, and close experiments with constitutional hygiene: clear hypotheses, bounded scope, honest reporting of results, and a clean separation from production |
| Involved lenses | EXPLORE-Q (primary researcher), TRUTH-Q (hypothesis and result validation), EVAL-Q (independent review), HUMAN-DIRECTOR (scope approval for large experiments) |
| Kernel services | `core/audit.py`, `core/scheduler.py`, `core/reflection.py`, `core/sabbath.py` |
| Key axioms | No action without audit; Research and production separation; Rest and protection are structural |
| Inputs | Experiment proposal (hypothesis, dataset, methodology, success criteria, scope bounds) |
| Outputs | Experiment record in `data/experiments/`; results report; AuditEvent `EXPERIMENT_CLOSED` |

---

## Flow

1. **Experiment proposal**
   - EXPLORE-Q (or HUMAN-DIRECTOR) opens an experiment with a written hypothesis and defined success criteria.
   - Scope bounds are declared: maximum compute, maximum duration, dataset(s) to use (all must be tagged `env: research`).
   - AuditEvent `EXPERIMENT_OPENED` is emitted.

2. **Execution**
   - Experiment runs are scheduled via `core/scheduler.py`; Sabbath windows are respected.
   - Each significant run emits a `EXPERIMENT_RUN` AuditEvent with parameters and metrics.

3. **Reflection checkpoint**
   - At each Sabbath-aligned reflection window, EXPLORE-Q pauses and asks:
     - Is the experiment still within its declared scope?
     - Are results honest (not cherry-picked)?
     - Should the hypothesis be revised?

4. **Closure and honest reporting**
   - All results — positive, negative, and inconclusive — are recorded.
   - TRUTH-Q reviews the results report for accuracy and completeness.
   - EVAL-Q independently reviews for cherry-picking or scope drift.
   - AuditEvent `EXPERIMENT_CLOSED` is emitted with final metrics and conclusion.

5. **Promotion gate trigger**
   - If results warrant a production model, EXPLORE-Q opens a P11 promotion request.
   - Experiments that do not warrant promotion are archived and may inform future experiments.

---

## Related files

- `src/models/experiment.py` – implementation.
- `config/model_policy.yaml` – compute limits, scope bounds, reflection checkpoint schedule.
