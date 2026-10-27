# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceContentParam"]


class InstanceContentParam(TypedDict, total=False):
    data: Required[str]
    """The content's values, serialized in `format`."""

    format: Required[Literal["json", "yaml", "jsonc", "xml", "csv", "text"]]
    """The serialization format of config content.

    A config instance is written to the device filesystem in this format.

    - `json`: standard JSON.
    - `yaml`: YAML 1.2.
    - `jsonc`: JSON with comments (JSON plus `//` and `/* */` comment syntax).
    - `xml`: XML.
    - `csv`: comma-separated values (RFC 4180).
    - `text`: plain, unstructured text with no specific format.
    """
