# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConfigTypeCreateParams"]


class ConfigTypeCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the config type."""

    slug: Required[str]
    """An immutable, code-friendly name for the config type."""
