# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .schema_document import SchemaDocument
from .schema_language import SchemaLanguage

__all__ = ["ConfigSchema"]


class ConfigSchema(BaseModel):
    id: str
    """ID of the config schema."""

    config_type_id: str
    """ID of the config type."""

    config_type_name: str
    """The name of the config type."""

    created_at: datetime
    """Timestamp of when the config schema was created."""

    digest: str
    """The digest of the config schema."""

    format: Literal["json", "yaml", "cue"]

    instance_filepath: str
    """
    The file path to deploy the config instance relative to
    `/srv/miru/config_instances`. `v1/motion-control.json` would deploy to
    `/srv/miru/config_instances/v1/motion-control.json`.
    """

    language: SchemaLanguage

    object: Literal["config_schema"]
    """The object type, which is always `config_schema`."""

    updated_at: datetime
    """Timestamp of when the config schema was last updated."""

    config_type: Optional["ConfigType"] = None
    """Expand the config type using 'expand=config_type' in the query string."""

    documents: Optional[List[SchemaDocument]] = None
    """
    Expand the config schema documents using `expand=documents` in the query string.
    """


from .config_type import ConfigType
