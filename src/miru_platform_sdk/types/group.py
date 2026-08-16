# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: str
    """ID of the group."""

    created_at: datetime
    """Timestamp of when the group was created."""

    name: str
    """Name of the group."""

    object: Literal["group"]
    """The object type, which is always `group`."""

    parent_id: Optional[str] = None
    """ID of the parent group. Null for top-level groups."""

    updated_at: datetime
    """Timestamp of when the group was last updated."""

    parent: Optional["Group"] = None
    """The parent group.

    Null for top-level groups. Expand using `expand=parent` in the query string.
    """
