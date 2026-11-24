# Task 03 — Docker Containerization

A full-stack application containerized using Docker and Docker Compose.

[![Task 04 CI/CD](https://github.com/AafiyaaBegam/task03-docker-containerization/actions/workflows/ci-cd.yml/badge.svg?branch=main)](https://github.com/AafiyaaBegam/task03-docker-containerization/actions/workflows/ci-cd.yml)

## Features
- Multi-stage Docker build
- FastAPI backend
- Vite frontend
- PostgreSQL and Redis services
- Health checks and persistent volumes
- Non-root application runtime

## Project Files
- `Dockerfile` — container image configuration
- `compose.yaml` — application and dependency services
- `main.py` — FastAPI application
- `requirements.txt` — Python dependencies
- `TASK-03-REPORT.md` — containerization report
- `TASK-04-CI-CD-REPORT.md` — automated CI/CD pipeline report
- `EVIDENCE-CHECKLIST.md` — verification checklist

## Task 04 — Automated CI/CD with GitHub Actions

The workflow at `.github/workflows/ci-cd.yml` runs automatically on pushes and pull requests targeting `main`, and can also be started manually.

Pipeline stages:
1. Install Python dependencies and CI tools.
2. Run Ruff lint checks and Python syntax validation.
3. Execute the pytest unit-test suite.
4. Validate the Docker Compose configuration.
5. Build the Docker image; authenticate to Docker Hub and publish the image on non-pull-request events using GitHub Actions secrets.

**Latest verified workflow run:** [Run #14 — successful](https://github.com/AafiyaaBegam/task03-docker-containerization/actions/runs/41023996433). Both the lint/test job and Docker build/push job completed successfully.

## Run Locally

Ensure Docker Desktop is installed and running. Then run:

```bash
docker compose build
docker compose up -d
```

Open `http://localhost:8000/health` to check the service.

**Note:** Verify the project folder structure and run the Docker build before claiming successful local execution.
