"""
Execution orchestration.

The Executor coordinates runtime execution and records
execution lifecycle events.
"""

from __future__ import annotations

from prooflight.events import Event
from prooflight.execution.context import ExecutionContext
from prooflight.runtime import Runtime


class Executor:
    """
    Coordinates execution of one experiment.
    """

    def __init__(
        self,
        runtime: Runtime,
    ) -> None:
        """
        Initialize executor.

        Parameters
        ----------
        runtime:
            Concrete runtime implementation.
        """

        self.runtime = runtime

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        """
        Execute one experiment.

        Lifecycle:

        execution.started
              |
              v
        runtime.execute()
              |
              v
        execution.completed

        If execution fails:

        execution.failed
        """

        context.recorder.record(
            Event(
                name="execution.started",
            )
        )

        try:
            self.runtime.execute(context)

        except Exception as exc:
            context.recorder.record(
                Event(
                    name="execution.failed",
                    payload={
                        "error": str(exc),
                        "error_type": type(exc).__name__,
                    },
                )
            )

            raise

        context.recorder.record(
            Event(
                name="execution.completed",
            )
        )
