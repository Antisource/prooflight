from pydantic import ValidationError

from prooflight.events import Event


def test_create_event() -> None:
    """A valid event can be created."""

    event = Event(name="runtime.started")

    assert event.name == "runtime.started"
    assert event.payload == {}


def test_empty_name_is_rejected() -> None:
    """Empty event names are invalid."""

    try:
        Event(name="   ")
    except ValidationError:
        return

    raise AssertionError("Expected ValidationError.")
