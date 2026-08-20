from __future__ import annotations

import json
from datetime import datetime
from typing import Callable

from sqlalchemy import select

from .clock import Clock
from .database import Database
from .errors import NotFoundError
from .events import append_outbox, append_public_event
from .identifiers import new_id
from .models import OutboxRecord, PublicEventRecord, ResearchRecord
from .runtime import FakeRuntime


class LifecycleService:
    def __init__(self, database: Database, runtime: FakeRuntime | None = None, clock: Clock | None = None):
        self.database = database
        self.clock = clock or Clock()
        self.runtime = runtime or FakeRuntime(database, self.clock)

    def create_research(self, commit_hook: Callable[[], None] | None = None) -> ResearchRecord:
        research_id = new_id()
        now = self.clock.now()
        with self.database.session() as session:
            try:
                row = ResearchRecord(id=research_id, status="CREATED", created_at=now, updated_at=now)
                session.add(row)
                append_outbox(session, research_id, "research.created", {"research_id": research_id, "status": "CREATED"}, self.clock)
                append_public_event(session, research_id, "research.created", {"status": "CREATED"}, self.clock)
                if commit_hook:
                    commit_hook()
                session.commit()
            except Exception:
                session.rollback()
                raise
        self.runtime.start(research_id)
        return row

    def get_research(self, research_id: str) -> ResearchRecord:
        with self.database.session() as session:
            row = session.get(ResearchRecord, research_id)
            if row is None:
                raise NotFoundError(f"research {research_id} not found")
            return row

    def list_events(self, research_id: str, after_sequence: int = 0) -> list[PublicEventRecord]:
        with self.database.session() as session:
            if session.get(ResearchRecord, research_id) is None:
                raise NotFoundError(f"research {research_id} not found")
            return list(
                session.scalars(
                    select(PublicEventRecord)
                    .where(PublicEventRecord.research_id == research_id, PublicEventRecord.sequence > after_sequence)
                    .order_by(PublicEventRecord.sequence)
                )
            )

    def outbox_rows(self, research_id: str) -> list[OutboxRecord]:
        with self.database.session() as session:
            return list(session.scalars(select(OutboxRecord).where(OutboxRecord.aggregate_id == research_id)))
