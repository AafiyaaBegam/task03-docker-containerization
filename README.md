# Task 03 — Docker Containerization

A full-stack application containerized using Docker and Docker Compose.

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
- `TASK-03-REPORT.md` — project report
- `EVIDENCE-CHECKLIST.md` — verification checklist

## Run Locally
Ensure Docker Desktop is installed and running. Then run:

```bash
docker compose build
docker compose up -d
```

Open `http://localhost:8000/health` to check the service.

**Note:** Verify the project folder structure and run the Docker build before claiming successful execution.
