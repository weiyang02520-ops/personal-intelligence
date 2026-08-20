from __future__ import annotations

from datetime import timedelta
from typing import Callable

from sqlalchemy import or_, select

from .clock import Clock
from .database import Database
from .identifiers import new_id
from .models import JobRecord


class JobService:
    def __init__(self, database: Database, clock: Clock | None = None, lease_seconds: int = 2):
        self.database = database
        self.clock = clock or Clock()
        self.lease_seconds = lease_seconds

    def enqueue(self, research_id: str) -> str:
        now = self.clock.now()
        job_id = new_id()
        with self.database.session() as session:
            session.add(JobRecord(id=job_id, research_id=research_id, status="QUEUED", attempts=0, available_at=now))
            session.commit()
        return job_id

    def claim_next(self) -> JobRecord | None:
        now = self.clock.now()
        with self.database.session() as session:
            row = session.scalar(
                select(JobRecord)
                .where(JobRecord.status == "QUEUED", JobRecord.available_at <= now)
                .order_by(JobRecord.available_at)
                .with_for_update(skip_locked=True)
            )
            if row is None:
                return None
            row.status = "RUNNING"
            row.attempts += 1
            row.heartbeat_at = now
            row.lease_until = now + timedelta(seconds=self.lease_seconds)
            session.commit()
            session.expunge(row)
            return row

    def heartbeat(self, job_id: str) -> bool:
        with self.database.session() as session:
            row = session.get(JobRecord, job_id)
            if row is None or row.status != "RUNNING":
                return False
            now = self.clock.now()
            row.heartbeat_at = now
            row.lease_until = now + timedelta(seconds=self.lease_seconds)
            session.commit()
            return True

    def complete(self, job_id: str) -> None:
        with self.database.session() as session:
            row = session.get(JobRecord, job_id)
            if row is None:
                return
            row.status = "COMPLETED"
            row.lease_until = None
            session.commit()

    def fail(self, job_id: str, error: str, retry: bool = True) -> None:
        with self.database.session() as session:
            row = session.get(JobRecord, job_id)
            if row is None:
                return
            row.last_error = error
            row.lease_until = None
            row.status = "QUEUED" if retry else "FAILED"
            row.available_at = self.clock.now() + timedelta(milliseconds=50)
            session.commit()

    def recover_stale(self) -> int:
        now = self.clock.now()
        with self.database.session() as session:
            rows = list(session.scalars(select(JobRecord).where(JobRecord.status == "RUNNING", JobRecord.lease_until < now)))
            for row in rows:
                row.status = "QUEUED"
                row.available_at = now
                row.lease_until = None
            session.commit()
            return len(rows)

    def run_once(self, work: Callable[[JobRecord], None]) -> bool:
        row = self.claim_next()
        if row is None:
            return False
        try:
            work(row)
        except Exception as exc:
            self.fail(row.id, str(exc), retry=True)
        else:
            self.complete(row.id)
        return True
