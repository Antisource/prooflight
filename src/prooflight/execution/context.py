"""
Execution context.

An ExecutionContext represents the state shared across a single experiment
execution.

It acts as a dependency boundary. Instead of passing many independent
objects between execution components, the context provides a single stable
interface.

The context currently contains:
- Experiment definition
- Event Recorder

Future components such as:
- Runtime
- Artifact Store
- Telemetry
- Evaluation state

will be added here when they become necessary.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from prooflight.domain import Experiment
from prooflight.recorder import Recorder


class ExecutionContext(BaseModel):
    """
    Immutable container for one experiment execution.

    A context belongs to exactly one execution lifecycle.

    Once created, the execution dependencies should not be replaced.
    This guarantees that every component participating in an execution
    observes the same execution state.
    """

    model_config = ConfigDict(
        frozen=True,
        arbitrary_types_allowed=True,
    )

    experiment: Experiment
    """
    Experiment specification being executed.
    """

    recorder: Recorder
    """
    Recorder responsible for collecting execution events.
    """
