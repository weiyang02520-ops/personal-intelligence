from __future__ import annotations

from apps.core.clock import FixedClock
from apps.core.errors import PocError
from apps.core.identifiers import new_id, require_id


def test_shared_concepts_are_stable():
    value = new_id()
    assert require_id(value) == value
    assert FixedClock.__name__ == "FixedClock"
    error = PocError("TEST", "message")
    assert {"code": error.code, "message": error.message} == {"code": "TEST", "message": "message"}
