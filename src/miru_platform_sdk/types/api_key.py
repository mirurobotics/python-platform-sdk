# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str
    """ID of the API key.

    Attribution fields such as `created_by_id` on other resources hold this ID when
    the API key performed the action.
    """

    created_at: datetime
    """Timestamp of when the API key was created."""

    created_by_id: str
    """ID of the user who created the API key."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the API key was deleted.

    Null if the API key is active. A deleted API key can no longer authenticate
    requests.
    """

    description: Optional[str] = None
    """A free-form description of the API key."""

    last_used_at: Optional[datetime] = None
    """Timestamp of when the API key last successfully authenticated a request.

    Null if the API key has never been used.
    """

    name: str
    """Name of the API key."""

    object: Literal["api_key"]
    """The object type, which is always `api_key`."""

    scopes: List[str]
    """Slugs of the scopes granted to the API key."""

    updated_at: datetime
    """Timestamp of when the API key was last updated."""
