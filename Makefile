.PHONY: fmt lint type test check

fmt:
	ruff check . --fix

lint:
	ruff check .

type:
	mypy src/textkit

test:
	pytest -q

check: lint type test