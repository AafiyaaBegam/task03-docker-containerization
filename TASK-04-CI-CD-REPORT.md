# Task 04 — Automated CI/CD Pipeline with GitHub Actions

## Objective

Automate code-quality checks, unit testing, container configuration validation, and Docker image publishing through GitHub Actions.

## Workflow

- Workflow file: `.github/workflows/ci-cd.yml`
- Workflow name: `Task 04 CI/CD`
- Triggers: pushes to `main`, pull requests targeting `main`, and manual `workflow_dispatch`
- Runner: `ubuntu-latest`
- Python runtime: `3.12`

## Pipeline stages

### 1. Lint and test

- Check out the repository.
- Install Python 3.12 and project dependencies.
- Install Ruff and pytest.
- Run `ruff check main.py --select E,F`.
- Compile-check `main.py` using `python -m py_compile main.py`.
- Run unit tests using `pytest -q`.
- Validate Compose configuration using `docker compose config --quiet`.

### 2. Docker build and publish

- Runs after the lint-and-test job succeeds.
- Authenticates to Docker Hub using repository Actions secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`.
- Builds the image from the repository Dockerfile.
- Publishes on push/manual events; pull-request events build without publishing.
- Tags the image as `aafiyaa/task03-docker-containerization:latest` and with the commit SHA.

## Verified execution

GitHub Actions run #14 completed successfully on 30 October 2026.

- Lint and test job: successful.
- Ruff lint: successful.
- Python syntax check: successful.
- pytest unit tests: successful.
- Docker Compose validation: successful.
- Docker Hub login: successful.
- Docker image build/publish action: successful.

Run evidence: https://github.com/AafiyaaBegam/task03-docker-containerization/actions/runs/41023996433

The repository README includes the live GitHub Actions status badge and links to the workflow.

## Security

Docker Hub credentials are referenced through GitHub Actions secrets and are not stored in the workflow file. Pull-request runs do not attempt to publish an image.

## Deliverables

- Workflow configuration: `.github/workflows/ci-cd.yml`
- Workflow status badge: repository README
- Pipeline documentation: `TASK-04-CI-CD-REPORT.md`
- Execution logs: linked GitHub Actions run above
