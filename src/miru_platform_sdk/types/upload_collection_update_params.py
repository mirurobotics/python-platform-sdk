# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UploadCollectionUpdateParams"]


class UploadCollectionUpdateParams(TypedDict, total=False):
    name: str
    """The updated name of the upload collection."""

    slug: str
    """The updated slug for the upload collection."""
