# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .user_status import UserStatus

__all__ = ["User"]


class User(BaseModel):
    id: str
    """ID of the user.

    Attribution fields such as `created_by_id` can also hold an API key's or a
    device's principal ID, which doesn't resolve to a user.
    """

    avatar_url: Optional[str] = None
    """The URL of the user's avatar image."""

    created_at: datetime
    """Timestamp of when the user was created."""

    email: str
    """The email address of the user."""

    first_name: str
    """The first name of the user."""

    last_name: str
    """The last name of the user."""

    object: Literal["user"]
    """The object type, which is always `user`."""

    status: UserStatus
    """The user's membership status."""

    updated_at: datetime
    """Timestamp of when the user was last updated."""
