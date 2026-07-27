# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .instance_content_param import InstanceContentParam

__all__ = ["ConfigInstanceCreateParams"]


class ConfigInstanceCreateParams(TypedDict, total=False):
    config_schema_id: Required[str]
    """The ID of the config schema which this config instance must adhere to."""

    content: Required[InstanceContentParam]

    expand: List[Literal["content", "config_schema", "config_type"]]
    """Fields to expand on the config instance resource."""

    slot_key: str
    """The slot of the config schema this instance is bound to.

    Optional when the schema has exactly one slot. Must match the `key` of one of
    the slots declared by the config schema.
    """
