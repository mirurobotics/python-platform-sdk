# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]

    id: SequenceNotStr[str]
    """The deployment IDs to filter by."""

    activity_status: List[Literal["drifted", "staged", "queued", "deployed", "archived"]]
    """The deployment activity statuses to filter by."""

    device_id: SequenceNotStr[str]
    """The deployment device IDs to filter by."""

    error_status: List[Literal["none", "failed", "retrying"]]
    """The deployment error statuses to filter by."""

    expand: List[Literal["total_count", "device", "release", "config_instances"]]
    """Fields to expand on each deployment in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]]
    """Sort order for the deployment results."""

    release_id: SequenceNotStr[str]
    """The deployment release IDs to filter by."""

    target_status: List[Literal["staged", "deployed", "archived"]]
    """The deployment target statuses to filter by."""
