
import os
from pathlib import Path

import psycopg
import redis
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://task03:local_only_change_me@localhost:5432/task03",
)
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Task 03 Containerization Demo", version="1.0.0")


def check_dependencies():
    status = {"postgres": "unavailable", "redis": "unavailable"}

    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=2) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
        status["postgres"] = "healthy"
    except Exception:
        pass

    try:
        client = redis.Redis.from_url(
            REDIS_URL,
            socket_connect_timeout=2,
            socket_timeout=2,
        )
        status["redis"] = "healthy" if client.ping() else "unavailable"
        client.close()
    except Exception:
        pass

    return status


@app.get("/health")
def health():
    deps = check_dependencies()
    ok = all(value == "healthy" for value in deps.values())

    return JSONResponse(
        status_code=200 if ok else 503,
        content={
            "status": "healthy" if ok else "degraded",
            "dependencies": deps,
        },
    )


@app.get("/api/info")
def info():
    return {
        "service": "Task 03 Containerization Demo",
        "database": "PostgreSQL",
        "cache": "Redis",
        "runtime": "non-root",
    }


if STATIC_DIR.exists() and (STATIC_DIR / "index.html").exists():
    app.mount(
        "/assets",
        StaticFiles(directory=STATIC_DIR / "assets"),
        name="assets",
    )

    @app.get("/", include_in_schema=False)
    def frontend():
        return FileResponse(STATIC_DIR / "index.html")
else:

    @app.get("/")
    def root():
        return {
            "message": (
                "Frontend assets are not built yet. "
                "Try /health or /api/info."
            )
        }
