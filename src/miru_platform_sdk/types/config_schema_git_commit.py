# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConfigSchemaGitCommit"]


class ConfigSchemaGitCommit(BaseModel):
    id: str
    """ID of the config schema git commit."""

    config_schema_id: str
    """ID of the associated config schema."""

    created_at: datetime
    """Timestamp of when the config schema git commit was created."""

    created_by_id: str
    """ID of the principal who created the config schema git commit."""

    file_paths: List[str]
    """The file paths of the config schema files relative to the git repository root.

    JSON Schema only support a single file for a schema. CUE support multiple files
    via [packages](https://cuelang.org/docs/references/spec/#packages).
    """

    git_commit_id: str
    """ID of the associated git commit."""

    object: Literal["config_schema_git_commit"]
    """The object type, which is always `config_schema_git_commit`."""
