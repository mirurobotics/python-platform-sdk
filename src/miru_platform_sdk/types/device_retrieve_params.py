# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DeviceRetrieveParams"]


class DeviceRetrieveParams(TypedDict, total=False):
    expand: List[Literal["current_deployment", "current_release"]]
    """Fields to expand on the device resource."""
