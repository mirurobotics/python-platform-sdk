# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["GitCommitListParams"]


class GitCommitListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """The git commit IDs to filter by."""

    expand: List[Literal["total_count"]]
    """Fields to expand on each git commit in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]]
    """Sort order for the git commit results."""

    sha: SequenceNotStr[str]
    """The git commit SHAs to filter by."""
