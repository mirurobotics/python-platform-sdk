# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ReleaseArchiveParams"]


class ReleaseArchiveParams(TypedDict, total=False):
    expand: List[Literal["config_schemas", "created_by", "archived_by"]]
    """Fields to expand on the release resource."""
