# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .upload_collection import UploadCollection
from .shared.paginated_list import PaginatedList

__all__ = ["UploadCollectionListResponse"]


class UploadCollectionListResponse(PaginatedList):
    data: List[UploadCollection]
    """The list of upload collections."""
