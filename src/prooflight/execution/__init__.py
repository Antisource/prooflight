"""
Execution lifecycle components.

This package contains objects responsible for managing the lifecycle
of an experiment execution.
"""

from .context import ExecutionContext
from .executor import Executor
from .result import ExecutionResult

__all__ = [
    "ExecutionContext",
    "Executor",
    "ExecutionResult",
]
