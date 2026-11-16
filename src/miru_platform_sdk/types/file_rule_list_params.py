# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["FileRuleListParams"]


class FileRuleListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """The file rule IDs to filter by."""

    bucket: SequenceNotStr[str]
    """The upload bucket names to filter by.

    A retention-only file rule, which has no `upload` block, never matches this
    filter.
    """

    expand: List[Literal["total_count"]]
    """Fields to expand on each file rule in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: List[Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc"]]
    """Sort order for the file rule results."""

    upload_collection_id: SequenceNotStr[str]
    """The upload collection IDs to filter by.

    A retention-only file rule, which has no `upload` block, never matches this
    filter.
    """

    upload_collection_slug: SequenceNotStr[str]
    """The upload collection slugs to filter by.

    A retention-only file rule, which has no `upload` block, never matches this
    filter.
    """
