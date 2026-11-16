# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeletedDevice"]


class DeletedDevice(BaseModel):
    id: str
    """The ID of the device."""

    deleted: bool
    """Whether the device was deleted."""

    object: Literal["device"]
    """The object type, which is always `device`."""
