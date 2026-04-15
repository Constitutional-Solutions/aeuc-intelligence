from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from core.sabbath import is_sabbath
from core.time_utils import now_utc


@dataclass
class Task:
    id: str
    lens_id: str
    payload: Dict[str, Any]
    created_at: Any


class Scheduler:
    """Minimal in-process task scheduler.

    This is intentionally small and in-memory. More advanced scheduling
    belongs in higher layers.
    """

    def __init__(self) -> None:
        self._queue: List[Task] = []

    def enqueue(self, lens_id: str, payload: Dict[str, Any]) -> Task:
        task = Task(id=f"task-{len(self._queue)+1}", lens_id=lens_id, payload=payload, created_at=now_utc())
        self._queue.append(task)
        return task

    def next_task(self) -> Optional[Task]:
        """Return the next task if one is available and we are not in Sabbath.

        For now this simply skips dispatching tasks during Sabbath; higher
        layers may override this logic for emergency work.
        """

        if not self._queue:
            return None

        if is_sabbath(now_utc()):
            return None

        return self._queue.pop(0)
