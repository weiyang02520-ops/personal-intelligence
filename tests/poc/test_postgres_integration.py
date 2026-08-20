from __future__ import annotations

import os
import time

import pytest
from sqlalchemy import func, select

from apps.core.database import Database
from apps.core.lifecycle import LifecycleService
from apps.core.models import OutboxRecord, ResearchRecord
from apps.core.clock import Clock
from apps.core.events import mark_processed
from apps.core.models import ProcessedEvent


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


@pytest.mark.integration
def test_postgresql_transaction_rollback_removes_research_and_outbox():
    url = os.getenv("POC_DATABASE_URL")
    if not url or not url.startswith("postgresql"):
        pytest.skip("POC_DATABASE_URL is not a PostgreSQL URL")
    db = Database(url)
    db.create_schema()
    service = LifecycleService(db)
    with db.session() as session:
        before_research = session.scalar(select(func.count(ResearchRecord.id)))
        before_outbox = session.scalar(select(func.count(OutboxRecord.id)))
    with pytest.raises(RuntimeError, match="postgres commit fault"):
        service.create_research(commit_hook=lambda: (_ for _ in ()).throw(RuntimeError("postgres commit fault")))
    with db.session() as session:
        assert session.scalar(select(func.count(ResearchRecord.id))) == before_research
        assert session.scalar(select(func.count(OutboxRecord.id))) == before_outbox


@pytest.mark.integration
def test_postgresql_duplicate_delivery_is_idempotent():
    url = os.getenv("POC_DATABASE_URL")
    if not url or not url.startswith("postgresql"):
        pytest.skip("POC_DATABASE_URL is not a PostgreSQL URL")
    db = Database(url)
    db.create_schema()
    event_id = f"postgres-event-{time.time_ns()}"
    with db.session() as session:
        assert mark_processed(session, "postgres-consumer", event_id, Clock()) is True
        session.commit()
    with db.session() as session:
        assert mark_processed(session, "postgres-consumer", event_id, Clock()) is False
        assert session.scalar(select(ProcessedEvent).where(ProcessedEvent.consumer == "postgres-consumer", ProcessedEvent.event_id == event_id)) is not None
