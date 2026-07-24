from pathlib import Path
from typing import Any, cast

import pytest
from pydantic import ValidationError

from prooflight.domain import Experiment


def make_experiment(**overrides: Any) -> Experiment:
    """Create a valid experiment for testing."""

    data: dict[str, Any] = {
        "name": "baseline",
        "runtime": "transformers",
        "agent": "react",
        "output_dir": Path("./artifacts"),
    }

    data.update(overrides)

    return Experiment(**data)


def test_create_valid_experiment() -> None:
    experiment = make_experiment()

    assert experiment.name == "baseline"
    assert experiment.runtime == "transformers"
    assert experiment.agent == "react"


def test_empty_name_is_rejected() -> None:
    with pytest.raises(ValidationError):
        make_experiment(name="   ")


def test_seed_must_be_non_negative() -> None:
    with pytest.raises(ValidationError):
        make_experiment(seed=-1)


def test_output_dir_is_normalized() -> None:
    experiment = make_experiment(output_dir=Path("~/prooflight"))

    assert experiment.output_dir.is_absolute()


def test_experiment_is_immutable() -> None:
    experiment = make_experiment()

    with pytest.raises(ValidationError, match="frozen"):
        cast(Any, experiment).name = "changed"
