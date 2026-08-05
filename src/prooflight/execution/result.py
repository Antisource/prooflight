"""
Execution result model.

Represents the final outcome of one experiment execution.

Events answer:
    "What happened during execution?"

ExecutionResult answers:
    "What was the final outcome?"
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class ExecutionResult(BaseModel):
    """
    Immutable result produced after execution completes.

    The result is intentionally separate from events.

    Events:
        - chronological execution history

    Result:
        - final execution summary
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    id: UUID = Field(
        default_factory=uuid4,
        description="Unique identifier for this execution result.",
    )

    status: str = Field(
        description="Final execution status.",
    )

    output: Any | None = Field(
        default=None,
        description="Execution output produced by runtime.",
    )

    error: str | None = Field(
        default=None,
        description="Error message if execution failed.",
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Time when result was created.",
    )
