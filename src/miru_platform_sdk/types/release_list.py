# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .release import Release
from .shared.paginated_list import PaginatedList

__all__ = ["ReleaseList"]


class ReleaseList(PaginatedList):
    data: List[Release]
    """The list of releases."""
