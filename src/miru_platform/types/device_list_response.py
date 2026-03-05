# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .device import Device
from .paginated_list import PaginatedList

__all__ = ["DeviceListResponse"]


class DeviceListResponse(PaginatedList):
    data: List[Device]
    """The list of devices."""
