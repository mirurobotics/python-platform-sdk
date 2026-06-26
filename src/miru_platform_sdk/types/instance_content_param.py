# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceContentParam"]


class InstanceContentParam(TypedDict, total=False):
    data: Required[str]
    """The configuration values associated with the config instance."""

    format: Required[Literal["json", "yaml", "jsonc"]]
    """
    The on-disk format used when a config instance is written to the device
    filesystem.

    - `json`: standard JSON.
    - `yaml`: YAML 1.2.
    - `jsonc`: JSON with comments (JSON plus `//` and `/* */` comment syntax).
    """
