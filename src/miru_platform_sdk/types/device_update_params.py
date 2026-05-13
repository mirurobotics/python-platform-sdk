# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DeviceUpdateParams"]


class DeviceUpdateParams(TypedDict, total=False):
    expand: List[Literal["current_deployment", "current_release"]]
    """Fields to expand on the device resource."""

    name: str
    """The new name of the device.

    If excluded from the request, the device name is not updated.
    """
