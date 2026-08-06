"""
Execution orchestration.

The Executor coordinates runtime execution,
records lifecycle events, and produces execution results.
"""

from __future__ import annotations

from prooflight.events import Event
from prooflight.execution.context import ExecutionContext
from prooflight.execution.result import ExecutionResult
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
        """

        self.runtime = runtime

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionResult:
        """
        Execute one experiment lifecycle.

        Returns
        -------
        ExecutionResult
            Final execution outcome.
        """

        context.recorder.record(
            Event(
                name="execution.started",
            )
        )

        try:
            output = self.runtime.execute(context)

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

            return ExecutionResult(
                status="failed",
                error=str(exc),
            )

        context.recorder.record(
            Event(
                name="execution.completed",
            )
        )

        return ExecutionResult(
            status="completed",
            output=output,
        )
