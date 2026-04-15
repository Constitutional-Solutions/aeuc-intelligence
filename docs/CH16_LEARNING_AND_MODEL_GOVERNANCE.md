# Chapter 16 – Learning, Research, and Model Governance

This chapter defines how the AEUC family governs the creation, evaluation, and deployment
of models, research tools, and learning systems.
It ties the freedom needed for research to the constitutional separation between research
and production established in Part I, and to the kernel's Sanctuary/Genesis/Gnosis layering.

---

## 16.1 Domain and primary axis

| Dimension | Value |
|---|---|
| Domain | Machine learning, research experimentation, model deployment, knowledge management |
| Primary axis | **Truth** |
| Love role | Protecting people from harmful or misleading model outputs |
| Power role | Legitimate authority over which models enter production and under what conditions |

---

## 16.2 Core tension this chapter resolves

Research requires freedom to explore, fail fast, and iterate without bureaucratic overhead.
Production requires stability, auditability, and human accountability.
This chapter defines the membrane between those two spaces so that both can coexist
without either compromising the other.

---

## 16.3 Lenses involved

| Lens ID | Role in this domain |
|---|---|
| HUMAN-DIRECTOR | Research lead and production approval authority |
| EXPLORE-Q | Research and experimentation; operates exclusively in `src/research/` |
| TRUTH-Q | Model evaluation: accuracy, calibration, known failure modes |
| RISK-Q | Risk scoring for model outputs (bias, safety, regulatory exposure) |
| AUDIT-Q | Compliance with data governance, privacy law, and applicable standards |
| SECURE-Q | Model artifact integrity; supply-chain security for weights and datasets |
| EVAL-Q | Independent model evaluation and cross-validation |

---

## 16.4 Research vs production boundary rules

- All experimental code lives in `src/research/`; production models in `src/models/`.
- A model cannot be promoted to production without:
  1. A completed evaluation report (EVAL-Q + TRUTH-Q).
  2. A RISK-Q risk score below the production threshold (defined in `config/model_policy.yaml`).
  3. HUMAN-DIRECTOR sign-off as an AuditEvent.
- Research datasets are tagged at ingestion; production datasets require AUDIT-Q approval.
- Model weights are hash-verified by SECURE-Q at every promotion and deployment step.

---

## 16.5 Pattern families in this chapter

| Pattern | Description |
|---|---|
| P09 – Dataset Ingestion and Provenance | Bringing data into the research or production environment with full lineage |
| P10 – Experiment Lifecycle | Designing, running, and closing experiments with constitutional hygiene |
| P11 – Model Evaluation and Promotion Gate | Structured evaluation before a model can enter production |
| P12 – Model Monitoring and Drift Response | Ongoing production monitoring and constitutionally-governed response to drift |

---

## 16.6 Key kernel services and extensions needed

- `core/audit.py` – wraps dataset ingestion, experiment runs, evaluation results, and promotions.
- `core/charter_kernel.py` – checked before every production promotion.
- `core/scheduler.py` – schedules periodic evaluation and drift-check tasks.
- `core/reflection.py` – learning retrospectives are structured as reflection windows.
- A future `src/models/promotion.py` will formalize the promotion gate referenced in
  Pattern P11.
- A `config/model_policy.yaml` will capture risk thresholds, framework identifiers,
  and monitoring parameters.

---

## 16.7 Relationship to advanced/quantum research track

The advanced research described in `docs/ADVANCED_QUANTUM_EXPANSION.md` is governed by the
same rules as any other research track:

- Experiments live in `src/research/`.
- No quantum-adjacent module enters `core/` or `src/models/` without going through P11.
- The Charter Kernel's integrity and the family's constitutional rhythms apply identically.

This keeps the most experimental work constitutionally contained without blocking exploration.

---

## 16.8 Next steps

Patterns P09–P12 will be written as individual pattern files in the next development cycle.
A `config/model_policy.yaml` will be created alongside them.
