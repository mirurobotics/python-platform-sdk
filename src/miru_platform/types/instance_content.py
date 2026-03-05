# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InstanceContent"]


class InstanceContent(BaseModel):
    data: str
    """The configuration values associated with the config instance."""

    format: Literal["json"]
