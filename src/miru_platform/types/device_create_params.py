# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeviceCreateParams"]


class DeviceCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the device."""

    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]
