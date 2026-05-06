# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .shared.paginated_list import PaginatedList

__all__ = ["DeviceList"]


class DeviceList(PaginatedList):
    data: List["Device"]
    """The list of devices."""


from .device import Device
