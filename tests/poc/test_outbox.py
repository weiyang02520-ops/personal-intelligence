from __future__ import annotations

import pytest
from sqlalchemy import select

from apps.core.database import Database
from apps.core.lifecycle import LifecycleService
from apps.core.models import OutboxRecord, ResearchRecord


def test_commit_failure_rolls_back_state_and_outbox(tmp_path):
    db = Database(f"sqlite:///{tmp_path / 'outbox.sqlite'}")
    db.create_schema()
    service = LifecycleService(db)
    with pytest.raises(RuntimeError, match="commit failure"):
        service.create_research(commit_hook=lambda: (_ for _ in ()).throw(RuntimeError("commit failure")))
    with db.session() as session:
        assert session.scalar(select(ResearchRecord)) is None
        assert session.scalar(select(OutboxRecord)) is None


def test_duplicate_publisher_delivery_has_one_consumer_effect(tmp_path):
    from apps.core.clock import Clock
    from apps.core.events import mark_processed

    db = Database(f"sqlite:///{tmp_path / 'idempotency.sqlite'}")
    db.create_schema()
    with db.session() as session:
        assert mark_processed(session, "consumer-a", "event-1", Clock()) is True
        session.commit()
    with db.session() as session:
        assert mark_processed(session, "consumer-a", "event-1", Clock()) is False
