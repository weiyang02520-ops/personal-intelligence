from __future__ import annotations

import ipaddress
import socket
from dataclasses import dataclass
from typing import Callable
from urllib.parse import urljoin, urlparse

import httpx

from .errors import ProviderError


@dataclass(frozen=True)
class FetchResult:
    url: str
    status_code: int
    content: bytes
    content_type: str
    provenance: dict[str, str]


def _blocked_ip(value: str) -> bool:
    ip = ipaddress.ip_address(value)
    return bool(ip.is_loopback or ip.is_private or ip.is_link_local or ip.is_reserved or ip.is_unspecified) or ip in {
        ipaddress.ip_address("169.254.169.254"),
        ipaddress.ip_address("100.100.100.200"),
    }


def default_resolver(host: str) -> list[str]:
    return list({item[4][0] for item in socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)})


class FetchGateway:
    def __init__(
        self,
        client: httpx.Client | None = None,
        resolver: Callable[[str], list[str]] = default_resolver,
        timeout: float = 5.0,
        max_bytes: int = 1_000_000,
        max_redirects: int = 3,
    ):
        self.client = client or httpx.Client(timeout=timeout, follow_redirects=False)
        self.resolver = resolver
        self.timeout = timeout
        self.max_bytes = max_bytes
        self.max_redirects = max_redirects

    def validate_url(self, url: str) -> None:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ProviderError("FETCH_UNSUPPORTED_URL", "only HTTP/HTTPS URLs are supported", 400)
        hostname = parsed.hostname.rstrip(".").lower()
        if hostname in {"localhost", "metadata.google.internal"} or hostname.endswith(".localhost"):
            raise ProviderError("FETCH_SSRF_BLOCKED", "local host is blocked", 403)
        try:
            addresses = [hostname] if _is_ip(hostname) else self.resolver(hostname)
        except (OSError, socket.gaierror, ValueError) as exc:
            raise ProviderError("FETCH_DNS_FAILED", "host could not be resolved", 502) from exc
        if not addresses or any(_blocked_ip(address) for address in addresses):
            raise ProviderError("FETCH_SSRF_BLOCKED", "resolved address is blocked", 403)

    def fetch(self, url: str) -> FetchResult:
        current = url
        for _ in range(self.max_redirects + 1):
            self.validate_url(current)
            try:
                response = self.client.get(current, timeout=self.timeout)
            except httpx.TimeoutException as exc:
                raise ProviderError("FETCH_TIMEOUT", "fetch timed out", 504) from exc
            except httpx.HTTPError as exc:
                raise ProviderError("FETCH_FAILED", "fetch transport failed", 502) from exc
            if response.is_redirect:
                location = response.headers.get("location")
                if not location:
                    raise ProviderError("FETCH_REDIRECT_INVALID", "redirect has no location", 502)
                current = urljoin(current, location)
                continue
            body = response.content
            if len(body) > self.max_bytes:
                raise ProviderError("FETCH_TOO_LARGE", "response exceeds configured size limit", 413)
            return FetchResult(
                url=str(response.url),
                status_code=response.status_code,
                content=body,
                content_type=response.headers.get("content-type", "application/octet-stream"),
                provenance={"requested_url": url, "final_url": str(response.url), "status_code": str(response.status_code)},
            )
        raise ProviderError("FETCH_TOO_MANY_REDIRECTS", "redirect limit exceeded", 502)


def _is_ip(hostname: str) -> bool:
    try:
        ipaddress.ip_address(hostname)
    except ValueError:
        return False
    return True
