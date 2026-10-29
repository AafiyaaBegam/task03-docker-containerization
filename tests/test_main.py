
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import main


def test_info_returns_service_details():
    result = main.info()

    assert result["service"] == "Task 03 Containerization Demo"
    assert result["database"] == "PostgreSQL"
    assert result["cache"] == "Redis"
    assert result["runtime"] == "non-root"


def test_check_dependencies_returns_unavailable_when_services_fail(
    monkeypatch,
):
    def fail_connection(*args, **kwargs):
        raise RuntimeError("Service unavailable")

    monkeypatch.setattr(main.psycopg, "connect", fail_connection)
    monkeypatch.setattr(main.redis.Redis, "from_url", fail_connection)

    result = main.check_dependencies()

    assert result == {
        "postgres": "unavailable",
        "redis": "unavailable",
    }


def test_root_fallback_message_when_frontend_is_missing(monkeypatch):
    monkeypatch.setattr(main, "STATIC_DIR", ROOT / "missing_test_static")

    result = main.root()

    assert "Frontend assets are not built yet" in result["message"]
