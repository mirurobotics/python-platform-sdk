# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["CalibrationListParams"]


class CalibrationListParams(TypedDict, total=False):
    aspect_id: SequenceNotStr[str]
    """The component aspect IDs to filter by."""

    component_id: SequenceNotStr[str]
    """The component IDs to filter by."""

    device_id: SequenceNotStr[str]
    """The device IDs to filter by."""

    expand: List[Literal["content", "total_count"]]
    """Fields to expand on each calibration in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    operator_id: SequenceNotStr[str]
    """The operator IDs to filter by."""

    order_by: List[
        Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc", "reported_at:asc", "reported_at:desc"]
    ]
    """Sort order for the calibration results."""

    report_id: SequenceNotStr[str]
    """The report IDs to filter by."""

    role_id: SequenceNotStr[str]
    """The component role IDs to filter by."""

    serial_number: SequenceNotStr[str]
    """The unit serial numbers to filter by."""
