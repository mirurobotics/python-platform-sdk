# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ComponentListParams"]


class ComponentListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """The component IDs to filter by."""

    device_id: SequenceNotStr[str]
    """The device IDs to filter by.

    Returns the components these devices have reported a calibration for.
    """

    expand: List[Literal["total_count", "roles", "aspects"]]
    """Fields to expand on each component in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    name: SequenceNotStr[str]
    """The component names to filter by."""

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
    """Sort order for the component results."""

    slug: SequenceNotStr[str]
    """The component slugs to filter by."""
