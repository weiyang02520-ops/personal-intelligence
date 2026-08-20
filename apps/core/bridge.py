from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .contracts import SearchRequest, SearchResponse
from .errors import PocError
from .search import SearchGateway


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: dict[str, Any]


class SearchToolBridge:
    """PI-controlled narrow bridge. Runtime never receives provider credentials."""

    ALLOWED = frozenset({"search"})

    def __init__(self, gateway: SearchGateway):
        self.gateway = gateway

    def invoke(self, call: ToolCall) -> SearchResponse:
        if call.name not in self.ALLOWED:
            raise PocError("TOOL_DENIED", f"tool {call.name!r} is not allowed", 403)
        query = str(call.arguments.get("query", ""))
        page = int(call.arguments.get("page", 1))
        per_page = int(call.arguments.get("per_page", 10))
        return self.gateway.search(SearchRequest(query=query, page=page, per_page=per_page))
