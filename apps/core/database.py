from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .models import Base


def default_database_url() -> str:
    return os.getenv("POC_DATABASE_URL", "sqlite:///./poc.db")


class Database:
    def __init__(self, url: str | None = None):
        self.url = url or default_database_url()
        connect_args = {"check_same_thread": False} if self.url.startswith("sqlite") else {}
        self.engine = create_engine(self.url, future=True, pool_pre_ping=True, connect_args=connect_args)
        self.sessions = sessionmaker(bind=self.engine, expire_on_commit=False, autoflush=False)

    def create_schema(self) -> None:
        Base.metadata.create_all(self.engine)

    @contextmanager
    def session(self) -> Iterator[Session]:
        session = self.sessions()
        try:
            yield session
        finally:
            session.close()
