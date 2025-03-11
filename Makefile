VENV = poetry run

LIBRARY = backlib
TESTS = tests


# CD
publish: publish-test publish-prod

publish-prod:
	poetry publish --dry-run

publish-test:
	poetry publish --dry-run --repository=test-pypi


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
