# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .upload import Upload
from .shared.paginated_list import PaginatedList

__all__ = ["UploadList"]


class UploadList(PaginatedList):
    data: List[Upload]
    """The list of uploads."""
