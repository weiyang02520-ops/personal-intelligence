from __future__ import annotations

import os
from typing import Any

import httpx

from .contracts import SearchItem, SearchProvider, SearchRequest, SearchResponse
from .errors import ProviderError


class FakeSearchProvider:
    name = "fake"

    def __init__(self, items: list[SearchItem] | None = None):
        self.items = items or []

    def search(self, request: SearchRequest) -> SearchResponse:
        start = (request.page - 1) * request.per_page
        page_items = self.items[start : start + request.per_page]
        return SearchResponse(page_items, request.page, start + request.per_page < len(self.items), self.name)


class GitHubSearchProvider:
    name = "github"
    endpoint = "https://api.github.com/search/repositories"

    def __init__(self, client: httpx.Client | None = None, token: str | None = None):
        self.client = client or httpx.Client(timeout=8.0)
        self.token = token if token is not None else os.getenv("POC_GITHUB_TOKEN")

    def search(self, request: SearchRequest) -> SearchResponse:
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "personal-intelligence-poc"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        try:
            response = self.client.get(
                self.endpoint,
                params={"q": request.query, "page": request.page, "per_page": request.per_page},
                headers=headers,
            )
        except httpx.TimeoutException as exc:
            raise ProviderError("SEARCH_TIMEOUT", "GitHub search timed out", 504) from exc
        except httpx.HTTPError as exc:
            raise ProviderError("SEARCH_PROVIDER_UNAVAILABLE", "GitHub search transport failed") from exc
        if response.status_code == 401:
            raise ProviderError("SEARCH_AUTH_FAILED", "GitHub search authentication failed", 502)
        if response.status_code == 429 or response.status_code == 403:
            raise ProviderError("SEARCH_RATE_LIMITED", "GitHub search rate limited", 429)
        if response.status_code >= 500:
            raise ProviderError("SEARCH_PROVIDER_UNAVAILABLE", "GitHub search unavailable")
        if response.status_code >= 400:
            raise ProviderError("SEARCH_PROVIDER_ERROR", f"GitHub search returned {response.status_code}")
        payload: dict[str, Any] = response.json()
        items = [
            SearchItem(
                title=str(item.get("full_name") or item.get("name") or ""),
                url=str(item.get("html_url") or ""),
                snippet=str(item.get("description") or ""),
                source="github",
                metadata={"stars": item.get("stargazers_count"), "language": item.get("language")},
            )
            for item in payload.get("items", [])
        ]
        total = int(payload.get("total_count") or 0)
        return SearchResponse(items, request.page, request.page * request.per_page < total, self.name, {"total_count": total})


class SearchGateway:
    def __init__(self, provider: SearchProvider):
        self.provider = provider

    def search(self, request: SearchRequest) -> SearchResponse:
        if not request.query.strip():
            raise ProviderError("SEARCH_INVALID_QUERY", "query must not be empty", 422)
        if request.page < 1 or request.per_page < 1 or request.per_page > 100:
            raise ProviderError("SEARCH_INVALID_PAGE", "invalid page or page size", 422)
        return self.provider.search(request)
