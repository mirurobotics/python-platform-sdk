# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DevicePingParams"]


class DevicePingParams(TypedDict, total=False):
    timeout_nanos: Required[int]
    """The timeout in nanoseconds to wait for the ping operation to complete.

    The maximum timeout is 10 seconds.
    """

    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]
