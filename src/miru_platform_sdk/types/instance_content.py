# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InstanceContent"]


class InstanceContent(BaseModel):
    data: str
    """The configuration values associated with the config instance."""

    format: Literal["json", "yaml", "jsonc"]
    """
    The on-disk format used when a config instance is written to the device
    filesystem.

    - `json`: standard JSON.
    - `yaml`: YAML 1.2.
    - `jsonc`: JSON with comments (JSON plus `//` and `/* */` comment syntax).
    """
