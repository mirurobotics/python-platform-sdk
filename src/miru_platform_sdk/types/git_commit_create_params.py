# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GitCommitCreateParams"]


class GitCommitCreateParams(TypedDict, total=False):
    message: Required[str]
    """The commit message."""

    origin: Required[str]
    """The URL of the git repository origin."""

    sha: Required[str]
    """The SHA hash of the git commit."""

    expand: List[Literal["created_by"]]
    """Fields to expand on the git commit resource."""
