# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroupMoveParams"]


class GroupMoveParams(TypedDict, total=False):
    parent_id: Required[Optional[str]]
    """ID of the new parent group. Set to null to make this a top-level group."""

    expand: List[Literal["parent"]]
    """Fields to expand on the group resource."""
