VENV = poetry run

LIBRARY = backlib
TESTS = tests


# Linters
lint: ruff mypy

mypy:
	$(VENV) mypy ./$(LIBRARY)/

ruff:
	$(VENV) ruff check ./$(LIBRARY)/ ./$(TESTS)/


# Tests
test: unit-tests

unit-tests:
	$(VENV) pytest ./$(TESTS)/
