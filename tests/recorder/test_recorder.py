from prooflight.events import Event
from prooflight.recorder import Recorder


def test_recorder_stores_events() -> None:
    """
    Recorder should preserve events in insertion order.
    """

    recorder = Recorder()

    first = Event(name="experiment.started")
    second = Event(name="experiment.finished")

    recorder.record(first)
    recorder.record(second)

    assert recorder.events == (
        first,
        second,
    )


def test_recorder_does_not_expose_mutable_storage() -> None:
    """
    Returned events should be immutable from the caller's perspective.
    """

    recorder = Recorder()

    recorder.record(Event(name="runtime.started"))

    events = recorder.events

    assert isinstance(events, tuple)
    assert len(events) == 1


def test_recorder_clear() -> None:
    """
    Recorder can reset its internal state.
    """

    recorder = Recorder()

    recorder.record(Event(name="test.event"))

    recorder.clear()

    assert recorder.events == ()
