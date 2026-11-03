# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .principal import Principal

__all__ = ["ConfigType"]


class ConfigType(BaseModel):
    id: str
    """ID of the config type."""

    archived_at: Optional[datetime] = None
    """Timestamp of when the config type was archived.

    Null if the config type is not archived.
    """

    archived_by_id: Optional[str] = None
    """ID of the principal who archived the config type.

    Null if the config type is not archived or was archived before this field was
    recorded.
    """

    created_at: datetime
    """Timestamp of when the config type was created."""

    created_by_id: str
    """ID of the principal who created the config type."""

    name: str
    """Name of the config type."""

    object: Literal["config_type"]
    """The object type, which is always `config_type`."""

    slug: str
    """An immutable, code-friendly name for the config type."""

    updated_at: datetime
    """Timestamp of when the config type was last updated."""

    updated_by_id: str
    """ID of the principal who last updated the config type."""

    archived_by: Optional[Principal] = None
    """The principal who archived the config type.

    Null if `archived_by_id` is null. Expand using `expand=archived_by` in the query
    string.
    """

    created_by: Optional[Principal] = None
    """The principal who created the config type.

    Expand using `expand=created_by` in the query string.
    """

    updated_by: Optional[Principal] = None
    """The principal who last updated the config type.

    Expand using `expand=updated_by` in the query string.
    """
