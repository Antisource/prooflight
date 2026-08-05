from pathlib import Path

from prooflight.domain import Experiment
from prooflight.execution import ExecutionContext, Executor
from prooflight.recorder import Recorder
from prooflight.runtime import Runtime


class SuccessfulRuntime(Runtime):
    """
    Runtime that completes successfully.
    """

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        pass


class FailingRuntime(Runtime):
    """
    Runtime that raises an error.
    """

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        raise RuntimeError("failed execution")


def create_context() -> ExecutionContext:
    """
    Create test execution context.
    """

    return ExecutionContext(
        experiment=Experiment(
            name="event-test",
            runtime="dummy",
            agent="test-agent",
            output_dir=Path("./artifacts"),
        ),
        recorder=Recorder(),
    )


def test_executor_records_success_events() -> None:
    """
    Successful execution should record started and completed events.
    """

    context = create_context()

    executor = Executor(
        runtime=SuccessfulRuntime(),
    )

    executor.execute(context)

    assert [event.name for event in context.recorder.events] == [
        "execution.started",
        "execution.completed",
    ]


def test_executor_records_failure_event() -> None:
    """
    Failed execution should record failed event.
    """

    context = create_context()

    executor = Executor(
        runtime=FailingRuntime(),
    )

    try:
        executor.execute(context)

    except RuntimeError:
        pass

    assert [event.name for event in context.recorder.events] == [
        "execution.started",
        "execution.failed",
    ]
