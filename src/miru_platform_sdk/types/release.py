# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .principal import Principal
from .config_schema import ConfigSchema

__all__ = ["Release"]


class Release(BaseModel):
    id: str
    """ID of the release."""

    archived_at: Optional[datetime] = None
    """Timestamp of when the release was archived.

    Null if the release is not archived.
    """

    archived_by_id: Optional[str] = None
    """ID of the principal who archived the release.

    Null if the release is not archived or was archived before this field was
    recorded.
    """

    created_at: datetime
    """Timestamp of when the release was created."""

    created_by_id: str
    """ID of the principal who created the release."""

    description: Optional[str] = None
    """A free-form description of the release."""

    git_commit_id: Optional[str] = None
    """The ID of the git commit associated with this release."""

    object: Literal["release"]
    """The object type, which is always `release`."""

    os: Literal["linux", "windows"]
    """An operating system family, from the agent's build-time OS vocabulary.

    Shared across resources (devices, config schemas, file rules, releases). This is
    the machine-readable OS kind, distinct from a human-readable version string.

    - `linux`
    - `windows`
    """

    updated_at: datetime
    """Timestamp of when the release was last updated."""

    version: str
    """The version of the release."""

    archived_by: Optional[Principal] = None
    """The principal who archived the release.

    Null if `archived_by_id` is null. Expand using `expand=archived_by` in the query
    string.
    """

    config_schemas: Optional[List[ConfigSchema]] = None
    """Expand the config schemas using 'expand=config_schemas' in the query string."""

    created_by: Optional[Principal] = None
    """The principal who created the release.

    Expand using `expand=created_by` in the query string.
    """
