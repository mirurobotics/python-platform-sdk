# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConfigInstanceDownloadParams"]


class ConfigInstanceDownloadParams(TypedDict, total=False):
    disposition: Literal["inline", "attachment"]
    """Controls the Content-Disposition behavior.

    Use `inline` to display in browser or `attachment` to trigger a file download.
    """
