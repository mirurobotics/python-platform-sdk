# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PrincipalIdentifyResponse"]


class PrincipalIdentifyResponse(BaseModel):
    id: str
    """ID of the principal."""

    name: str
    """The display name of the principal."""

    object: Literal["principal"]
    """The object type, which is always `principal`."""
