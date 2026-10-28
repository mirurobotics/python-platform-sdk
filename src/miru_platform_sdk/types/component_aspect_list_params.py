# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ComponentAspectListParams"]


class ComponentAspectListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """The component aspect IDs to filter by."""

    component_id: SequenceNotStr[str]
    """The component IDs to filter by."""

    expand: List[Literal["total_count", "component"]]
    """Fields to expand on each component aspect in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    name: SequenceNotStr[str]
    """The component aspect names to filter by."""

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
            "slug:asc",
            "slug:desc",
        ]
    ]
    """Sort order for the component aspect results."""

    slug: SequenceNotStr[str]
    """The component aspect slugs to filter by."""
