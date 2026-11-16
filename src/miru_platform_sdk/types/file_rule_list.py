# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .file_rule import FileRule
from .shared.paginated_list import PaginatedList

__all__ = ["FileRuleList"]


class FileRuleList(PaginatedList):
    data: List[FileRule]
    """The list of file rules."""
