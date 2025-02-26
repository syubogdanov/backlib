LIBRARY = backlib
VENV = poetry run


# Linters
lint: ruff mypy

mypy:
	$(VENV) mypy ./$(LIBRARY)/

ruff:
	$(VENV) ruff check ./$(LIBRARY)/


# Tests
test: unit-tests

unit-tests:
	$(VENV) pytest ./tests/
