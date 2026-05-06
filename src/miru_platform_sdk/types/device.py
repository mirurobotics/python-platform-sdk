# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .release import Release
from .._models import BaseModel

__all__ = ["Device"]


class Device(BaseModel):
    id: str
    """ID of the device."""

    agent_version: Optional[str] = None
    """The version of the agent the device is running."""

    created_at: datetime
    """Timestamp of when the device was created."""

    last_connected_at: Optional[datetime] = None
    """
    Timestamp of when the device was last made an initial connection (this is not
    the same as the last time the device was seen).
    """

    last_disconnected_at: Optional[datetime] = None
    """
    Timestamp of when the device was last disconnected (this is not the same as the
    last time the device was seen).
    """

    name: str
    """Name of the device."""

    object: Literal["device"]
    """The object type, which is always `device`."""

    status: Literal["inactive", "activating", "online", "offline"]
    """The status of the device.

    - Inactive: The miru agent has not yet been installed / authenticated
    - Activating: The miru agent is currently being installed / authenticated
      (should only last for a few seconds)
    - Online: The miru agent has successfully pinged the server within the last 60
      seconds.
    - Offline: The miru agent has not successfully pinged the server within the last
      60 seconds (e.g. network issues, device is powered off, etc.)
    """

    updated_at: datetime
    """Timestamp of when the device was last updated."""

    current_deployment: Optional["Deployment"] = None
    """The current deployment for the device."""

    current_release: Optional[Release] = None
    """The current release for the device."""


from .deployment import Deployment
