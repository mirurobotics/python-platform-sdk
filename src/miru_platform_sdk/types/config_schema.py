# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .config_type import ConfigType
from .instance_slot import InstanceSlot
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

    instance_format: Literal["json", "yaml", "jsonc", "xml", "text"]
    """
    The on-disk format used when a config instance is written to the device
    filesystem.

    - `json`: standard JSON.
    - `yaml`: YAML 1.2.
    - `jsonc`: JSON with comments (JSON plus `//` and `/* */` comment syntax).
    - `xml`: XML.
    - `text`: plain, unstructured text with no specific format.
    """

    instance_slots: List[InstanceSlot]
    """The file system destinations this config schema writes to.

    Every config schema has at least one slot. Slots share the schema's validation
    and differ only in where the file is written; a file needing different
    validation is a different config type, not a slot. Slot keys and filepaths must
    each be unique within the schema, and slot filepaths must be unique across every
    config schema in a release.
    """

    language: SchemaLanguage

    object: Literal["config_schema"]
    """The object type, which is always `config_schema`."""

    updated_at: datetime
    """Timestamp of when the config schema was last updated."""

    config_type: Optional[ConfigType] = None
    """Expand the config type using 'expand=config_type' in the query string."""

    documents: Optional[List[SchemaDocument]] = None
    """
    Expand the config schema documents using `expand=documents` in the query string.
    """
