from __future__ import annotations

import json
import time
from dataclasses import asdict
from typing import Iterator

from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from .database import Database
from .errors import PocError, ValidationError
from .lifecycle import LifecycleService


class CreateResearchRequest(BaseModel):
    title: str | None = Field(default=None, max_length=200)


class ResearchResponse(BaseModel):
    id: str
    status: str
    created_at: str
    updated_at: str


def _response(row) -> ResearchResponse:
    return ResearchResponse(id=row.id, status=row.status, created_at=row.created_at.isoformat(), updated_at=row.updated_at.isoformat())


def create_app(database_url: str | None = None) -> FastAPI:
    database = Database(database_url)
    database.create_schema()
    service = LifecycleService(database)
    app = FastAPI(title="Personal Intelligence Physical Architecture PoC")
    app.state.database = database
    app.state.lifecycle = service

    @app.exception_handler(PocError)
    async def poc_error_handler(_: Request, exc: PocError):
        return JSONResponse(status_code=exc.status_code, content={"error": {"code": exc.code, "message": exc.message, "request_id": None}})

    @app.post("/research", response_model=ResearchResponse, status_code=202)
    def create_research(_: CreateResearchRequest):
        return _response(service.create_research())

    @app.get("/research/{research_id}", response_model=ResearchResponse)
    def get_research(research_id: str):
        return _response(service.get_research(research_id))

    @app.get("/research/{research_id}/events")
    def events(research_id: str, after_sequence: int = Query(default=0, ge=0)):
        def stream() -> Iterator[str]:
            cursor = after_sequence
            deadline = time.monotonic() + 10
            while time.monotonic() < deadline:
                rows = service.list_events(research_id, cursor)
                for row in rows:
                    cursor = row.sequence
                    payload = {"type": row.event_type, "sequence": row.sequence, "data": json.loads(row.payload)}
                    yield f"id: {cursor}\nevent: public\ndata: {json.dumps(payload, sort_keys=True)}\n\n"
                current = service.get_research(research_id)
                if current.status in {"COMPLETED", "CANCELLED", "FAILED"} and not service.list_events(research_id, cursor):
                    break
                time.sleep(0.02)

        return StreamingResponse(stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache"})

    return app


app = create_app()
