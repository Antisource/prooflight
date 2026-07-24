"""
Immutable experiment definition.

An Experiment describes a single evaluation. It contains configuration only and
is safe to serialize, compare, and reproduce.
"""

from pathlib import Path
from typing import TypeAlias
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator

JsonPrimitive: TypeAlias = str | int | float | bool | None
JsonValue: TypeAlias = JsonPrimitive | list[JsonPrimitive] | dict[str, JsonPrimitive]


class Experiment(BaseModel):
    """Immutable specification for one evaluation experiment."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    id: UUID = Field(default_factory=uuid4)

    name: str = Field(
        min_length=1,
        description="Human-readable experiment name.",
    )

    runtime: str = Field(
        description="Registered runtime identifier.",
    )

    agent: str = Field(
        description="Registered agent identifier.",
    )

    tasks: tuple[str, ...] = ()

    mitigations: tuple[str, ...] = ()

    seed: int = Field(
        default=42,
        ge=0,
        description="Random seed for reproducibility.",
    )

    output_dir: Path

    metadata: dict[str, JsonValue] = Field(default_factory=dict)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Experiment name cannot be empty.")

        return value

    @field_validator("output_dir")
    @classmethod
    def normalize_output_dir(cls, value: Path) -> Path:
        return value.expanduser().resolve()
