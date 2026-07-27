# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InstanceSlot"]


class InstanceSlot(BaseModel):
    filepath: str
    """The absolute file system path where instances bound to this slot are written.

    Must be unique within the schema, and unique across every config schema in a
    release.
    """

    key: str
    """An immutable, code-friendly identifier for this slot, unique within the schema.

    Lowercase alphanumerics, underscores, and hyphens; must start with an
    alphanumeric; at most 128 characters.
    """

    name: str
    """The human-readable name of this slot."""

    required: bool
    """
    Whether every deployment of a release containing this schema must include an
    instance for this slot. A deployment includes at most one config instance per
    slot.
    """

    description: Optional[str] = None
    """An optional human-readable description of this slot."""
