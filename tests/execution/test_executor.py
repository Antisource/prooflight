from pathlib import Path

from prooflight.domain import Experiment
from prooflight.execution import ExecutionContext, Executor
from prooflight.recorder import Recorder
from prooflight.runtime import Runtime


class RecordingRuntime(Runtime):
    """
    Runtime implementation used to verify Executor behaviour.
    """

    def __init__(self) -> None:
        self.executed = False

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        """
        Mark execution as completed.
        """

        self.executed = True


def create_context() -> ExecutionContext:
    """
    Create a minimal execution context.
    """

    experiment = Experiment(
        name="executor-test",
        runtime="dummy",
        agent="test-agent",
        output_dir=Path("./artifacts"),
    )

    return ExecutionContext(
        experiment=experiment,
        recorder=Recorder(),
    )


def test_executor_delegates_to_runtime() -> None:
    """
    Executor should delegate execution to Runtime.
    """

    runtime = RecordingRuntime()

    executor = Executor(
        runtime=runtime,
    )

    executor.execute(
        create_context(),
    )

    assert runtime.executed is True
