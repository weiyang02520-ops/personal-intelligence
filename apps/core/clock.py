from __future__ import annotations

from datetime import datetime, timezone


class Clock:
    def now(self) -> datetime:
        return datetime.now(timezone.utc)


class FixedClock(Clock):
    def __init__(self, value: datetime):
        self.value = value if value.tzinfo else value.replace(tzinfo=timezone.utc)

    def now(self) -> datetime:
        return self.value
