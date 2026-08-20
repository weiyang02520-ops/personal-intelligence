from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PocError(Exception):
    code: str
    message: str
    status_code: int = 400

    def __str__(self) -> str:
        return self.message


class NotFoundError(PocError):
    def __init__(self, message: str = "resource not found"):
        super().__init__("NOT_FOUND", message, 404)


class SecretNotFound(PocError):
    def __init__(self, name: str):
        super().__init__("SECRET_NOT_FOUND", f"secret {name!r} was not found", 404)


class ValidationError(PocError):
    def __init__(self, message: str):
        super().__init__("VALIDATION_ERROR", message, 422)


class ProviderError(PocError):
    def __init__(self, code: str, message: str, status_code: int = 502):
        super().__init__(code, message, status_code)
