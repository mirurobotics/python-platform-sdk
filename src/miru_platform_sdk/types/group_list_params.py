# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """The group IDs to filter by."""

    expand: List[Literal["total_count", "parent", "ancestors"]]
    """Fields to expand on each group in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    name: SequenceNotStr[str]
    """The group names to filter by."""

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: List[
        Literal[
            "id:asc",
            "id:desc",
            "created_at:asc",
            "created_at:desc",
            "updated_at:asc",
            "updated_at:desc",
            "name:asc",
            "name:desc",
        ]
    ]
    """Sort order for the group results."""

    parent_id: SequenceNotStr[str]
    """The parent group IDs to filter by."""
