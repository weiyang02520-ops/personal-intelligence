from __future__ import annotations

from pathlib import Path

import pytest

from apps.core.api import create_app


@pytest.fixture()
def app(tmp_path: Path):
    return create_app(f"sqlite:///{tmp_path / 'poc.sqlite'}")
