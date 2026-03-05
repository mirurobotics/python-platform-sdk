# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GitCommitRefParam"]


class GitCommitRefParam(TypedDict, total=False):
    """A reference to a git commit.

    At least one of `id` or `sha` must be provided. When both are provided, `id` takes precedence and `sha` is ignored.
    """

    id: str
    """ID of the git commit. Takes precedence over `sha` when both are provided."""

    sha: str
    """The SHA hash of the git commit. Used only when `id` is not provided."""
