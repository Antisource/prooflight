from pathlib import Path

from prooflight.domain import Experiment
from prooflight.execution import ExecutionContext
from prooflight.recorder import Recorder
from prooflight.runtime import Runtime


class DummyRuntime(Runtime):
    """
    Minimal runtime implementation for testing.

    Real runtimes will provide concrete execution behaviour.
    """

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        """
        Execute a dummy evaluation.
        """

        return None


def create_context() -> ExecutionContext:
    """
    Create a minimal execution context.
    """

    experiment = Experiment(
        name="runtime-test",
        runtime="dummy",
        agent="test-agent",
        output_dir=Path("./artifacts"),
    )

    return ExecutionContext(
        experiment=experiment,
        recorder=Recorder(),
    )


def test_runtime_can_be_implemented() -> None:
    """
    Concrete runtimes should satisfy the Runtime contract.
    """

    runtime = DummyRuntime()

    assert isinstance(runtime, Runtime)


def test_runtime_execute_accepts_context() -> None:
    """
    Runtime execution should receive an ExecutionContext.
    """

    runtime = DummyRuntime()

    runtime.execute(create_context())
