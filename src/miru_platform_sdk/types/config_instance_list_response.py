# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .shared.paginated_list import PaginatedList

__all__ = ["ConfigInstanceListResponse"]


class ConfigInstanceListResponse(PaginatedList):
    data: List["ConfigInstance"]
    """The list of config instances."""


from .config_instance import ConfigInstance
