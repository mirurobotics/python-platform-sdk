# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GitCommitCreateParams"]


class GitCommitCreateParams(TypedDict, total=False):
    message: Required[str]
    """The commit message."""

    origin: Required[str]
    """The URL of the git repository origin."""

    sha: Required[str]
    """The SHA hash of the git commit."""

    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]
