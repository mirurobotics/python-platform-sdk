# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeletedRelease"]


class DeletedRelease(BaseModel):
    id: str
    """ID of the deleted release."""

    deleted: bool
    """Whether the release was deleted."""

    object: Literal["release"]
    """The object type, which is always `release`."""
