# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ConfigSchemaRetrieveParams"]


class ConfigSchemaRetrieveParams(TypedDict, total=False):
    expand: List[Literal["documents", "config_type"]]
    """Fields to expand on the config schema resource."""
