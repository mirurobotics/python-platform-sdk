# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConfigInstanceDownloadContentParams"]


class ConfigInstanceDownloadContentParams(TypedDict, total=False):
    miru_version: Required[Annotated[str, PropertyInfo(alias="Miru-Version")]]

    disposition: Literal["inline", "attachment"]
    """Controls the Content-Disposition behavior.

    Use `inline` to display in browser or `attachment` to trigger a file download.
    """
