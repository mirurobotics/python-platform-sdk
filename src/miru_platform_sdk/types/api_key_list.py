# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .api_key import APIKey
from .shared.paginated_list import PaginatedList

__all__ = ["APIKeyList"]


class APIKeyList(PaginatedList):
    data: List[APIKey]
    """The list of API keys."""
