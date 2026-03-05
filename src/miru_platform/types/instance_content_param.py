# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceContentParam"]


class InstanceContentParam(TypedDict, total=False):
    data: Required[str]
    """The configuration values associated with the config instance."""

    format: Required[Literal["json"]]
