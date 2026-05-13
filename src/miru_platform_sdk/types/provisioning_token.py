# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ProvisioningToken"]


class ProvisioningToken(BaseModel):
    token: str
    """The provisioning token. This value is only returned when the token is created."""

    expires_at: datetime
    """The expiration date and time of the token."""
