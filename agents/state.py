from dataclasses import dataclass, field
from typing import Any, Optional
from typing_extensions import TypedDict

class AgentState(TypedDict):
    objective: str                        # e.g. "maximize F1 under p95 < 20ms"
    dataset_path: str
    constraints: dict                   

    runs: list[dict]                      # list of {config, metrics, model_uri, passed_constraints}
    best_run: Optional[dict]

    max_runs: int
    runs_remaining: int

    decision: Optional[str]
    rejection_reason: Optional[str]
    promotion_report_path: Optional[str]
