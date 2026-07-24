PACKAGE := src/prooflight
TESTS := tests

.PHONY: format lint typecheck test check

format:
	uv run ruff format $(PACKAGE) $(TESTS)

lint:
	uv run ruff check $(PACKAGE) $(TESTS)

typecheck:
	uv run mypy src tests

test:
	uv run pytest

check:
	uv run ruff check $(PACKAGE) $(TESTS)
	uv run mypy src tests
	uv run pytest