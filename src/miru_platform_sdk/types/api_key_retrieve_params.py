# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["APIKeyRetrieveParams"]


class APIKeyRetrieveParams(TypedDict, total=False):
    expand: List[Literal["created_by"]]
    """Fields to expand on the API key resource."""
