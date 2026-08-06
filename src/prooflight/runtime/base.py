"""
Runtime abstraction.

A Runtime represents an executable environment capable of running
an evaluation.

Concrete implementations may wrap:

- language models
- agent frameworks
- external APIs
- simulation environments

The base Runtime does not implement execution logic.
It only defines the contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from prooflight.execution import ExecutionContext


class Runtime(ABC):
    """
    Abstract execution backend.

    Every runtime must provide an execute method.

    Examples of future implementations:

    - TransformersRuntime
    - OpenAIRuntime
    - LangGraphRuntime
    - LocalAgentRuntime
    """

    @abstractmethod
    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        """
        Execute one evaluation.

        Parameters
        ----------
        context:
            Complete state of the current execution.

        Returns
        -------
        None
            Execution results are currently recorded through events.
            Future versions will introduce structured results.
        """

        raise NotImplementedError
