# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .git_commit_ref_param import GitCommitRefParam

__all__ = ["ReleaseCreateParams"]


class ReleaseCreateParams(TypedDict, total=False):
    config_schema_ids: Required[SequenceNotStr[str]]
    """The IDs of the config schemas included in the release."""

    version: Required[str]
    """The version of the release."""

    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]

    expand: List[Literal["config_schemas"]]
    """Fields to expand on the release resource."""

    git_commit_ref: GitCommitRefParam
    """A reference to a git commit.

    At least one of `id` or `sha` must be provided. When both are provided, `id`
    takes precedence and `sha` is ignored.
    """
