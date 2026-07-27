# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceSlotParam"]


class InstanceSlotParam(TypedDict, total=False):
    filepath: Required[str]
    """The absolute file system path where instances bound to this slot are written.

    Must be unique within the schema, and unique across every config schema in a
    release.
    """

    key: Required[str]
    """An immutable, code-friendly identifier for this slot, unique within the schema.

    Lowercase alphanumerics, underscores, and hyphens; must start with an
    alphanumeric; at most 128 characters.
    """

    name: Required[str]
    """The human-readable name of this slot."""

    required: Required[bool]
    """
    Whether every deployment of a release containing this schema must include an
    instance for this slot. A deployment includes at most one config instance per
    slot.
    """

    description: str
    """An optional human-readable description of this slot."""
