# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .principal_type import PrincipalType

__all__ = ["Principal"]


class Principal(BaseModel):
    id: str
    """ID of the principal."""

    name: str
    """The display name of the principal."""

    object: Literal["principal"]
    """The object type, which is always `principal`."""

    type: PrincipalType
    """The kind of principal. More types may be added, so handle unknown values."""
