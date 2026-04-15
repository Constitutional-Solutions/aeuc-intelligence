"""Pattern P10 – Experiment Lifecycle."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List

from core.audit import audit
from core.time_utils import now_utc


@dataclass
class ExperimentRecord:
    experiment_id: str
    proposer_id: str
    hypothesis: str
    success_criteria: str
    dataset_ids: List[str]
    opened_at: datetime = field(default_factory=now_utc)
    status: str = "open"  # open | closed
    runs: List[Dict[str, Any]] = field(default_factory=list)


def open_experiment(experiment_id: str, proposer_id: str, hypothesis: str, success_criteria: str, dataset_ids: List[str]) -> ExperimentRecord:
    record = ExperimentRecord(
        experiment_id=experiment_id,
        proposer_id=proposer_id,
        hypothesis=hypothesis,
        success_criteria=success_criteria,
        dataset_ids=dataset_ids,
    )
    with audit("EXPERIMENT_OPENED", lens_id=proposer_id, details={"experiment_id": experiment_id}):
        pass
    return record


def close_experiment(record: ExperimentRecord, conclusion: str, lens_id: str) -> None:
    record.status = "closed"
    with audit("EXPERIMENT_CLOSED", lens_id=lens_id, details={"experiment_id": record.experiment_id, "conclusion": conclusion}):
        pass
