# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConfigTypeCreateParams"]


class ConfigTypeCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the config type."""

    slug: Required[str]
    """An immutable, code-friendly name for the config type."""

    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]

    expand: List[Literal["config_schemas"]]
    """Fields to expand on the config type resource."""
