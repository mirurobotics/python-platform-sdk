# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .git_commit import GitCommit
from .paginated_list import PaginatedList

__all__ = ["GitCommitListResponse"]


class GitCommitListResponse(PaginatedList):
    data: List[GitCommit]
    """The list of git commits."""
