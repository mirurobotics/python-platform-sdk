# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UploadCollection"]


class UploadCollection(BaseModel):
    id: str
    """ID of the upload collection."""

    created_at: datetime
    """Timestamp of when the upload collection was created."""

    name: str
    """Name of the upload collection."""

    object: Literal["upload_collection"]
    """The object type, which is always `upload_collection`."""

    slug: str
    """An immutable, code-friendly name for the upload collection."""

    updated_at: datetime
    """Timestamp of when the upload collection was last updated."""
