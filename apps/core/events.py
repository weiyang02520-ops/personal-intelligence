from __future__ import annotations

import json
from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .clock import Clock
from .identifiers import new_id
from .models import OutboxRecord, ProcessedEvent, PublicEventRecord


def append_outbox(session: Session, aggregate_id: str, event_type: str, payload: dict, clock: Clock) -> OutboxRecord:
    record = OutboxRecord(
        id=new_id(),
        aggregate_id=aggregate_id,
        event_type=event_type,
        payload=json.dumps(payload, sort_keys=True),
        created_at=clock.now(),
    )
    session.add(record)
    return record


def append_public_event(session: Session, research_id: str, event_type: str, payload: dict, clock: Clock) -> PublicEventRecord:
    last = session.scalar(select(func.max(PublicEventRecord.sequence)).where(PublicEventRecord.research_id == research_id)) or 0
    record = PublicEventRecord(
        id=new_id(),
        research_id=research_id,
        sequence=last + 1,
        event_type=event_type,
        payload=json.dumps(payload, sort_keys=True),
        created_at=clock.now(),
    )
    session.add(record)
    return record


def mark_processed(session: Session, consumer: str, event_id: str, clock: Clock) -> bool:
    existing = session.scalar(select(ProcessedEvent).where(ProcessedEvent.consumer == consumer, ProcessedEvent.event_id == event_id))
    if existing is not None:
        return False
    session.add(ProcessedEvent(id=new_id(), consumer=consumer, event_id=event_id, processed_at=clock.now()))
    return True
