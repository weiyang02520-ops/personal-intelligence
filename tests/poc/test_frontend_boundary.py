from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).parents[2]


def test_frontend_calls_pi_api_only():
    text_files = {".ts", ".tsx", ".json", ".css", ".d.ts"}
    source = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "apps" / "web").rglob("*") if path.is_file() and path.suffix in text_files and "node_modules" not in path.parts and ".next" not in path.parts)
    forbidden = ("deer-flow", "langgraph", "POC_GITHUB_TOKEN", "Authorization")
    assert not any(value.lower() in source.lower() for value in forbidden)
    assert "/research" in source and "/events" in source
