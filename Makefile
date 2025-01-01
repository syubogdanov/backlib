DOCKER = docker
VENV = poetry run

# Docker
docker:
	$(DOCKER) build --file ./dev/docker/py39.Dockerfile --tag backlib:3.9 .
	$(DOCKER) build --file ./dev/docker/py310.Dockerfile --tag backlib:3.10 .
	$(DOCKER) build --file ./dev/docker/py311.Dockerfile --tag backlib:3.11 .
	$(DOCKER) build --file ./dev/docker/py312.Dockerfile --tag backlib:3.12 .
	$(DOCKER) build --file ./dev/docker/py313.Dockerfile --tag backlib:3.13 .

# Linters
lint: ruff mypy

mypy:
	$(VENV) mypy ./

ruff:
	$(VENV) ruff check ./

# Tests
test: unit-tests compatibility-tests

unit-tests:
	$(VENV) pytest ./tests/

compatibility-tests:
	$(DOCKER) run backlib:3.9 -B -m pytest ./tests/
	$(DOCKER) run backlib:3.10 -B -m pytest ./tests/
	$(DOCKER) run backlib:3.11 -B -m pytest ./tests/
	$(DOCKER) run backlib:3.12 -B -m pytest ./tests/
	$(DOCKER) run backlib:3.13 -B -m pytest ./tests/
