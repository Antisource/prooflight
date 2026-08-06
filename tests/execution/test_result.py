from prooflight.execution import ExecutionResult


def test_execution_result_is_immutable() -> None:
    """
    Execution results should not change after creation.
    """

    result = ExecutionResult(
        status="completed",
        output="success",
    )

    try:
        result.status = "failed"  # type: ignore[misc]

    except Exception:
        return

    raise AssertionError("ExecutionResult should be immutable.")


def test_execution_result_stores_output() -> None:
    """
    Result should preserve execution output.
    """

    result = ExecutionResult(
        status="completed",
        output={"answer": 42},
    )

    assert result.status == "completed"
    assert result.output == {"answer": 42}
