# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    expand: List[Literal["parent"]]
    """Fields to expand on the group resource."""

    name: str
    """The updated name of the group."""
