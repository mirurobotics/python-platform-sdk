# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DeviceBulkMoveParams"]


class DeviceBulkMoveParams(TypedDict, total=False):
    device_ids: Required[SequenceNotStr[str]]
    """IDs of the devices to move."""

    target_group_id: Required[Optional[str]]
    """ID of the target group. Set to null to unassign all listed devices."""

    expand: List[Literal["total_count", "current_deployment", "current_release", "group"]]
    """Fields to expand on each device in the list."""
