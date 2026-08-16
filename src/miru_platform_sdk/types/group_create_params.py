# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the group."""

    expand: List[Literal["parent"]]
    """Fields to expand on the group resource."""

    parent_id: Optional[str]
    """ID of the parent group. Omit or set to null to create a top-level group."""
