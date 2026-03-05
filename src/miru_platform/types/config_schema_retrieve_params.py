# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConfigSchemaRetrieveParams"]


class ConfigSchemaRetrieveParams(TypedDict, total=False):
    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]

    expand: List[Literal["documents", "config_type"]]
    """Fields to expand on the config schema resource."""
