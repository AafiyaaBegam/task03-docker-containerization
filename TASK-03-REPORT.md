# Task 03 — Multi-Stage Docker Containerization & Optimization

## Objective
Package a small full-stack service using Docker multi-stage builds and Docker Compose. Keep build tools out of the runtime image, run the application as a non-root user, and orchestrate PostgreSQL and Redis with health checks and persistent storage.

## Architecture
The Node/Vite build stage produces static assets that are copied into the Python runtime image. FastAPI serves the frontend and `/health` endpoint. PostgreSQL and Redis are private Compose-network services, not published on host ports.

## Multi-stage build
1. `frontend-build` uses Node Alpine to produce static browser assets.
2. `python-deps` installs Python packages into a separate prefix.
3. `runtime` copies only application code, built assets, and installed dependencies into a Python Alpine image.

Compiler packages and Node tooling are excluded from the runtime stage. The final image size depends on actual dependency/base-image layers and must be measured locally.

## Security and reliability
- Application process uses UID/GID `10001`, not root.
- Docker and Compose health checks call the application health endpoint or native dependency health commands.
- PostgreSQL and Redis use named volumes.
- PostgreSQL is not exposed directly to the host.
- `.env` is excluded from Git and Docker build context.
- The sample password is for local use only. Change it before any non-local deployment.

For production, add managed secrets, pinned image digests, vulnerability scanning, TLS, resource limits, and tested backup/restore procedures.

## Build and run
Run from the repository root in PowerShell:

```powershell
Copy-Item .env.example .env
docker compose build
docker compose up -d
docker compose ps
Invoke-RestMethod http://localhost:8000/health
```

## Verify image size and non-root execution
```powershell
docker image inspect task03-docker-containerization-app:local --format='{{.Size}}'
docker inspect task03-docker-containerization-app --format='User={{.Config.User}}'
docker compose logs --tail=100 app
```

The image inspection command returns bytes. Divide by 1,048,576 to convert to MiB. The assignment target is below 150 MB; do not claim the target is met until the actual built image has been measured.

Expected health response when both dependencies are available:

```json
{
  "status": "healthy",
  "dependencies": {
    "postgres": "healthy",
    "redis": "healthy"
  }
}
```

This is the expected response shape, not captured execution evidence. If health returns `503`, inspect `docker compose logs app db redis`.

## Persistence note
The Compose file defines named volumes for PostgreSQL and Redis. The included demo verifies dependency connectivity and configures persistence, but it does not implement a business data-write endpoint. If the rubric requires proof of persisted application records, add and test a write/read flow before claiming that requirement is complete.

## Evidence required
Capture genuine terminal output or screenshots for the successful build, `docker compose ps`, health response, measured image size, runtime user, and relevant logs. Save the results in `docs/evidence/`. Never fabricate logs or claim a test passed without running it.

## Conclusion
The project provides a practical multi-stage full-stack containerization example with non-root execution, health checks, and Compose-managed PostgreSQL/Redis. Runtime acceptance criteria must be verified in the target Docker environment.
