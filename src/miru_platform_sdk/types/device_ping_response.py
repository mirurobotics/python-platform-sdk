# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DevicePingResponse"]


class DevicePingResponse(BaseModel):
    code: Literal["success", "timeout"]
    """The result of the ping operation."""

    round_trip_nanos: Optional[int] = None
    """
    The round trip time in nanoseconds to send the ping to the device and receive
    the response. Only present when `code` is `success`.
    """
