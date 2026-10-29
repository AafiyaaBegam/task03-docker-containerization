
from main import check_dependencies, info, root


def test_info_returns_service_details():
    result = info()

    assert result["service"] == "Task 03 Containerization Demo"
    assert result["database"] == "PostgreSQL"
    assert result["cache"] == "Redis"
    assert result["runtime"] == "non-root"


def test_check_dependencies_returns_expected_keys(monkeypatch):
    import main

    monkeypatch.setattr(
        main.psycopg,
        "connect",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            RuntimeError("Database unavailable")
        ),
    )
    monkeypatch.setattr(
        main.redis.Redis,
        "from_url",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            RuntimeError("Redis unavailable")
        ),
    )

    result = check_dependencies()

    assert set(result.keys()) == {"postgres", "redis"}
    assert result["postgres"] == "unavailable"
    assert result["redis"] == "unavailable"


def test_root_returns_fallback_message():
    import main

    if not (
        main.STATIC_DIR.exists()
        and (main.STATIC_DIR / "index.html").exists()
    ):
        result = root()
        assert "Frontend assets are not built yet" in result["message"]
