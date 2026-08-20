from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable, Protocol


@dataclass(frozen=True)
class RuntimeEvent:
    event_type: str
    data: dict[str, Any] = field(default_factory=dict)


class RuntimePort(Protocol):
    def start(self, research_id: str) -> None: ...

    def cancel(self, research_id: str) -> bool: ...

    def capabilities(self) -> dict[str, bool]: ...


@dataclass(frozen=True)
class SearchRequest:
    query: str
    page: int = 1
    per_page: int = 10


@dataclass(frozen=True)
class SearchItem:
    title: str
    url: str
    snippet: str = ""
    source: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SearchResponse:
    items: list[SearchItem]
    page: int
    has_more: bool
    provider: str
    raw_metadata: dict[str, Any] = field(default_factory=dict)


class SearchProvider(Protocol):
    name: str

    def search(self, request: SearchRequest) -> SearchResponse: ...


class FetchPort(Protocol):
    def fetch(self, url: str) -> Any: ...


class SecretStore(Protocol):
    def put(self, name: str, value: str) -> None: ...

    def get(self, name: str) -> str: ...
