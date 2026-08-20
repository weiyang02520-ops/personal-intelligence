from __future__ import annotations

import httpx
import pytest

from apps.core.bridge import SearchToolBridge, ToolCall
from apps.core.contracts import SearchItem, SearchRequest
from apps.core.errors import PocError, ProviderError
from apps.core.search import FakeSearchProvider, GitHubSearchProvider, SearchGateway


def test_fake_search_normalizes_pagination_and_provenance():
    provider = FakeSearchProvider([SearchItem(str(i), f"https://example.test/{i}") for i in range(3)])
    result = SearchGateway(provider).search(SearchRequest("query", page=2, per_page=2))
    assert [item.title for item in result.items] == ["2"]
    assert result.provider == "fake" and result.has_more is False


@pytest.mark.parametrize(
    ("status", "code"),
    [(401, "SEARCH_AUTH_FAILED"), (403, "SEARCH_RATE_LIMITED"), (429, "SEARCH_RATE_LIMITED"), (503, "SEARCH_PROVIDER_UNAVAILABLE")],
)
def test_github_error_contract(status, code):
    transport = httpx.MockTransport(lambda request: httpx.Response(status, request=request))
    provider = GitHubSearchProvider(httpx.Client(transport=transport), token="test-only-token")
    with pytest.raises(ProviderError) as error:
        provider.search(SearchRequest("pi"))
    assert error.value.code == code


def test_github_success_and_no_result_contract():
    def handler(request):
        assert request.url.params["q"] == "personal intelligence"
        assert request.headers["authorization"] == "Bearer test-only-token"
        return httpx.Response(200, json={"total_count": 0, "items": []}, request=request)

    provider = GitHubSearchProvider(httpx.Client(transport=httpx.MockTransport(handler)), token="test-only-token")
    result = provider.search(SearchRequest("personal intelligence"))
    assert result.items == [] and result.has_more is False and result.raw_metadata["total_count"] == 0


def test_search_timeout_and_gateway_validation():
    def timeout(_):
        raise httpx.ReadTimeout("timeout")

    provider = GitHubSearchProvider(httpx.Client(transport=httpx.MockTransport(timeout)))
    with pytest.raises(ProviderError, match="timed out"):
        provider.search(SearchRequest("pi"))
    with pytest.raises(ProviderError) as error:
        SearchGateway(provider).search(SearchRequest(" "))
    assert error.value.code == "SEARCH_INVALID_QUERY"


def test_tool_bridge_allowlist_keeps_provider_inside_pi_boundary():
    gateway = SearchGateway(FakeSearchProvider([SearchItem("one", "https://example.test/one")]))
    bridge = SearchToolBridge(gateway)
    assert bridge.invoke(ToolCall("search", {"query": "one"})).items[0].title == "one"
    with pytest.raises(PocError) as error:
        bridge.invoke(ToolCall("fetch_url", {"url": "https://example.test"}))
    assert error.value.code == "TOOL_DENIED"
