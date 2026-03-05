# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .paginated_list import PaginatedList

__all__ = ["ConfigTypeListResponse"]


class ConfigTypeListResponse(PaginatedList):
    data: List["ConfigType"]
    """The list of config types."""


from .config_type import ConfigType
