# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .git_commit_ref_param import GitCommitRefParam

__all__ = ["ConfigSchemaCreateParams", "ConfigTypeRef", "Document", "GitCommit"]


class ConfigSchemaCreateParams(TypedDict, total=False):
    config_type_ref: Required[ConfigTypeRef]
    """A reference to a config type.

    At least one of `id` or `slug` must be provided. When both are provided, `id`
    takes precedence and `slug` is ignored.
    """

    documents: Required[Iterable[Document]]
    """The schema document files."""

    format: Required[Literal["json", "yaml", "cue"]]

    language: Required[Literal["jsonschema", "cue"]]

    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]

    expand: List[Literal["documents", "config_type"]]
    """Fields to expand on the config schema resource."""

    git_commit: GitCommit
    """The git commit to link to this config schema."""

    instance_filepath: str
    """The file path for config instances created from this schema."""


class ConfigTypeRef(TypedDict, total=False):
    """A reference to a config type.

    At least one of `id` or `slug` must be provided. When both are provided, `id` takes precedence and `slug` is ignored.
    """

    id: str
    """ID of the config type. Takes precedence over `slug` when both are provided."""

    slug: str
    """An immutable, code-friendly name for the config type.

    Used only when `id` is not provided.
    """


class Document(TypedDict, total=False):
    data: Required[str]
    """The raw document content."""

    name: Required[str]
    """The name of this document."""


class GitCommit(TypedDict, total=False):
    """The git commit to link to this config schema."""

    commit_ref: Required[GitCommitRefParam]
    """A reference to a git commit.

    At least one of `id` or `sha` must be provided. When both are provided, `id`
    takes precedence and `sha` is ignored.
    """

    schema_filepaths: Required[SequenceNotStr[str]]
    """The file paths of the config schema files relative to the git repository root.

    JSON Schema only supports a single file for a schema. CUE support multiple files
    via [packages](https://cuelang.org/docs/references/spec/#packages).
    """
