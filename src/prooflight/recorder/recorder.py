"""
Execution event recorder.

The Recorder is responsible for collecting immutable events produced during
an experiment execution.

It intentionally has a small interface. Persistence, exporting, and artifact
generation will be handled later by the Artifact Store layer.
"""

from __future__ import annotations

from prooflight.events import Event


class Recorder:
    """
    Stores events generated during one execution.

    A Recorder belongs to a single execution context. It should not be shared
    across independent experiments.
    """

    def __init__(self) -> None:
        """
        Initialize an empty event history.

        Internally events are stored as a list because execution order matters.
        The first event happened before the second event, and that ordering is
        important for replay and debugging.
        """

        self._events: list[Event] = []

    def record(self, event: Event) -> None:
        """
        Append a new event to the execution history.

        Parameters
        ----------
        event:
            Immutable event produced by any execution component.
        """

        self._events.append(event)

    @property
    def events(self) -> tuple[Event, ...]:
        """
        Return all recorded events.

        A tuple is returned instead of the internal list so callers cannot
        accidentally mutate the recorder's history.
        """

        return tuple(self._events)

    def clear(self) -> None:
        """
        Remove all recorded events.

        This is mainly useful for testing. In normal execution, a recorder
        represents the complete lifetime of one experiment.
        """

        self._events.clear()
