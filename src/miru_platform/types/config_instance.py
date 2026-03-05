# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .instance_content import InstanceContent

__all__ = ["ConfigInstance"]


class ConfigInstance(BaseModel):
    id: str
    """ID of the config instance."""

    config_schema_id: str
    """ID of the config schema which the config instance must adhere to."""

    config_type_id: str
    """ID of the config type which the config instance (and its schema) is a part of."""

    config_type_name: str
    """The name of the config type."""

    created_at: datetime
    """The timestamp of when the config instance was created."""

    filepath: str
    """
    The file path to deploy the config instance relative to
    `/srv/miru/config_instances`. `v1/motion-control.json` would deploy to
    `/srv/miru/config_instances/v1/motion-control.json`.
    """

    object: Literal["config_instance"]
    """The object type, which is always `config_instance`."""

    config_schema: Optional["ConfigSchema"] = None
    """Expand the config schema using 'expand=config_schema' in the query string."""

    config_type: Optional["ConfigType"] = None
    """Expand the config type using 'expand=config_type' in the query string."""

    content: Optional[InstanceContent] = None
    """The configuration values associated with the config instance.

    Expand the content using 'expand=content' in the query string.
    """


from .config_type import ConfigType
from .config_schema import ConfigSchema
