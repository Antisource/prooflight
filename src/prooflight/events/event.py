"""
Immutable execution event.

Events are the fundamental record of everything that happens during an
experiment. They are intentionally generic so that new event types can be
introduced without changing the core event model.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Event(BaseModel):
    """Immutable execution event."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    id: UUID = Field(
        default_factory=uuid4,
        description="Unique identifier for the event.",
    )

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Time at which the event occurred.",
    )

    name: str = Field(
        min_length=1,
        description="Machine-readable event name.",
    )

    payload: dict[str, Any] = Field(
        default_factory=dict,
        description="Structured event data.",
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Reject empty event names."""

        value = value.strip()

        if not value:
            raise ValueError("Event name cannot be empty.")

        return value
