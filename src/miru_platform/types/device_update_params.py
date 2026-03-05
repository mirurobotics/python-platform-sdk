# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeviceUpdateParams"]


class DeviceUpdateParams(TypedDict, total=False):
    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]

    name: str
    """The new name of the device.

    If excluded from the request, the device name is not updated.
    """
