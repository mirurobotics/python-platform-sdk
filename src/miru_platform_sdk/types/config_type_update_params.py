# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConfigTypeUpdateParams"]


class ConfigTypeUpdateParams(TypedDict, total=False):
    name: str
    """The updated name of the config type."""

    slug: str
    """The updated slug for the config type."""
