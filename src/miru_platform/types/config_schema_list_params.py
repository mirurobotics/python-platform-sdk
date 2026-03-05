# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ConfigSchemaListParams"]


class ConfigSchemaListParams(TypedDict, total=False):
    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]

    id: SequenceNotStr[str]
    """The config schema IDs to filter by."""

    config_type_id: SequenceNotStr[str]
    """The config type IDs to filter by."""

    expand: List[Literal["total_count", "documents", "config_type"]]
    """Fields to expand on each config schema in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]]
    """Sort order for the config schema results."""
