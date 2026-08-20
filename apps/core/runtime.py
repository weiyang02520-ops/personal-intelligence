from __future__ import annotations

import threading
import time

from .clock import Clock
from .database import Database
from .events import append_public_event
from .models import ResearchRecord


class FakeRuntime:
    """PoC runtime. It owns no Product Core types and writes through the service boundary."""

    def __init__(self, database: Database, clock: Clock | None = None):
        self.database = database
        self.clock = clock or Clock()
        self._cancelled: set[str] = set()

    def start(self, research_id: str) -> None:
        thread = threading.Thread(target=self._execute, args=(research_id,), daemon=True)
        thread.start()

    def cancel(self, research_id: str) -> bool:
        self._cancelled.add(research_id)
        return True

    def capabilities(self) -> dict[str, bool]:
        return {"start": True, "events": True, "result": True, "cancel": True, "resume": False}

    def _execute(self, research_id: str) -> None:
        with self.database.session() as session:
            row = session.get(ResearchRecord, research_id)
            if row is None:
                return
            row.status = "RUNNING_LIKE"
            row.updated_at = self.clock.now()
            append_public_event(session, research_id, "research.running", {"status": row.status}, self.clock)
            session.commit()
        time.sleep(0.05)
        with self.database.session() as session:
            row = session.get(ResearchRecord, research_id)
            if row is None:
                return
            if research_id in self._cancelled:
                row.status = "CANCELLED"
                event_type = "research.cancelled"
            else:
                row.status = "COMPLETED"
                event_type = "research.completed"
            row.updated_at = self.clock.now()
            append_public_event(session, research_id, event_type, {"status": row.status}, self.clock)
            session.commit()
