from __future__ import annotations

import httpx
import pytest

from apps.core.errors import ProviderError
from apps.core.fetch import FetchGateway


def gateway(handler, resolver=None, max_bytes=100):
    client = httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=False)
    return FetchGateway(client=client, resolver=resolver or (lambda _: ["93.184.216.34"]), max_bytes=max_bytes)


def test_bounded_fetch_returns_provenance():
    def handler(request):
        return httpx.Response(200, headers={"content-type": "text/plain"}, content=b"hello", request=request)

    result = gateway(handler).fetch("https://example.test/page")
    assert result.content == b"hello"
    assert result.provenance["requested_url"] == "https://example.test/page"
    assert result.provenance["final_url"] == "https://example.test/page"


@pytest.mark.parametrize("url", [
    "http://localhost/admin",
    "http://127.0.0.1/admin",
    "http://169.254.169.254/latest/meta-data",
    "http://10.0.0.4/private",
])
def test_ssrf_targets_are_blocked(url):
    fetcher = gateway(lambda request: httpx.Response(200, request=request))
    with pytest.raises(ProviderError) as error:
        fetcher.fetch(url)
    assert error.value.code == "FETCH_SSRF_BLOCKED"


def test_private_dns_answer_is_blocked():
    fetcher = gateway(lambda request: httpx.Response(200, request=request), resolver=lambda _: ["192.168.1.10"])
    with pytest.raises(ProviderError) as error:
        fetcher.fetch("https://attacker.example")
    assert error.value.code == "FETCH_SSRF_BLOCKED"


def test_redirect_is_revalidated_and_bounded():
    def handler(request):
        return httpx.Response(302, headers={"location": "http://127.0.0.1/secret"}, request=request)

    with pytest.raises(ProviderError) as error:
        gateway(handler).fetch("https://example.test/redirect")
    assert error.value.code == "FETCH_SSRF_BLOCKED"


def test_response_size_is_bounded():
    fetcher = gateway(lambda request: httpx.Response(200, content=b"12345", request=request), max_bytes=4)
    with pytest.raises(ProviderError) as error:
        fetcher.fetch("https://example.test/large")
    assert error.value.code == "FETCH_TOO_LARGE"
