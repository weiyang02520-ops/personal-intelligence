from __future__ import annotations

import os
import time

import pytest
from sqlalchemy import select

from apps.core.database import Database
from apps.core.lifecycle import LifecycleService
from apps.core.models import OutboxRecord, ResearchRecord


@pytest.mark.integration
def test_postgresql_candidate_a_lifecycle_and_outbox():
    url = os.getenv("POC_DATABASE_URL")
    if not url or not url.startswith("postgresql"):
        pytest.skip("POC_DATABASE_URL is not a PostgreSQL URL")
    db = Database(url)
    db.create_schema()
    service = LifecycleService(db)
    row = service.create_research()
    deadline = time.monotonic() + 3
    while time.monotonic() < deadline:
        if service.get_research(row.id).status == "COMPLETED":
            break
        time.sleep(0.02)
    assert service.get_research(row.id).status == "COMPLETED"
    with db.session() as session:
        assert session.get(ResearchRecord, row.id) is not None
        assert session.scalar(select(OutboxRecord).where(OutboxRecord.aggregate_id == row.id)) is not None
