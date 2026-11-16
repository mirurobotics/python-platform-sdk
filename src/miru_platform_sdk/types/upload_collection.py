# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .principal import Principal

__all__ = ["UploadCollection"]


class UploadCollection(BaseModel):
    id: str
    """ID of the upload collection."""

    archived_at: Optional[datetime] = None
    """Timestamp of when the upload collection was archived.

    Null if the upload collection is not archived.
    """

    archived_by_id: Optional[str] = None
    """ID of the principal who archived the upload collection.

    Null if the upload collection is not archived or was archived before this field
    was recorded.
    """

    created_at: datetime
    """Timestamp of when the upload collection was created."""

    created_by_id: str
    """ID of the principal who created the upload collection."""

    name: str
    """Name of the upload collection."""

    object: Literal["upload_collection"]
    """The object type, which is always `upload_collection`."""

    slug: str
    """An immutable, code-friendly name for the upload collection."""

    updated_at: datetime
    """Timestamp of when the upload collection was last updated."""

    archived_by: Optional[Principal] = None
    """The principal who archived the upload collection.

    Null if `archived_by_id` is null. Expand using `expand=archived_by` in the query
    string.
    """

    created_by: Optional[Principal] = None
    """The principal who created the upload collection.

    Expand using `expand=created_by` in the query string.
    """
