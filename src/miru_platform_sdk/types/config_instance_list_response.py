# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .config_instance import ConfigInstance
from .shared.paginated_list import PaginatedList

__all__ = ["ConfigInstanceListResponse"]


class ConfigInstanceListResponse(PaginatedList):
    data: List[ConfigInstance]
    """The list of config instances."""
