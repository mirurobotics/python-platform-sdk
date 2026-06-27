# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UploadCollectionCreateParams"]


class UploadCollectionCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the upload collection."""

    slug: Required[str]
    """An immutable, code-friendly name for the upload collection."""
