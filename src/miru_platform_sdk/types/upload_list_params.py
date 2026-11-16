# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .upload_status import UploadStatus

__all__ = ["UploadListParams"]


class UploadListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """The upload IDs to filter by."""

    bundle_id: SequenceNotStr[str]
    """The upload bundle IDs to filter by."""

    device_id: SequenceNotStr[str]
    """The device IDs to filter by."""

    expand: List[Literal["total_count"]]
    """Fields to expand on each upload in the list."""

    file_rule_id: SequenceNotStr[str]
    """The file rule IDs to filter by."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: List[
        Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc", "uploaded_at:asc", "uploaded_at:desc"]
    ]
    """Sort order for the upload results."""

    status: List[UploadStatus]
    """The upload statuses to filter by."""

    upload_collection_id: SequenceNotStr[str]
    """The upload collection IDs to filter by."""
