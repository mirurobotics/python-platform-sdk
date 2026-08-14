# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeviceCreateParams"]


class DeviceCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the device."""

    expand: List[Literal["current_deployment", "current_release", "group"]]
    """Fields to expand on the device resource."""
