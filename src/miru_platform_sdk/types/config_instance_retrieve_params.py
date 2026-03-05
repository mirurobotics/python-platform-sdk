# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ConfigInstanceRetrieveParams"]


class ConfigInstanceRetrieveParams(TypedDict, total=False):
    expand: List[Literal["content", "config_schema", "config_type"]]
    """Fields to expand on the config instance resource."""
