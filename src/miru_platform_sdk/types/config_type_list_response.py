# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .config_type import ConfigType
from .shared.paginated_list import PaginatedList

__all__ = ["ConfigTypeListResponse"]


class ConfigTypeListResponse(PaginatedList):
    data: List[ConfigType]
    """The list of config types."""
