from pathlib import Path

from prooflight.domain import Experiment
from prooflight.execution import ExecutionContext
from prooflight.recorder import Recorder


def create_experiment() -> Experiment:
    """
    Create a minimal valid experiment for testing.
    """

    return Experiment(
        name="context-test",
        runtime="mock",
        agent="test-agent",
        output_dir=Path("./artifacts"),
    )


def test_execution_context_stores_dependencies() -> None:
    """
    ExecutionContext should store the dependencies required
    for a single execution.
    """

    experiment = create_experiment()
    recorder = Recorder()

    context = ExecutionContext(
        experiment=experiment,
        recorder=recorder,
    )

    assert context.experiment == experiment
    assert context.recorder == recorder


def test_execution_context_is_frozen() -> None:
    """
    ExecutionContext should enforce immutability.
    """

    assert ExecutionContext.model_config.get("frozen") is True
