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

    arch: Optional[str] = None
    """
    The CPU architecture the device is running, reported by the agent from its
    build-time architecture vocabulary (for example `x86_64` or `aarch64`).
    """

    created_at: datetime
    """Timestamp of when the device was created."""

    description: Optional[str] = None
    """A free-form description of the device."""

    group_id: Optional[str] = None
    """ID of the group this device belongs to. Null if the device is unassigned."""

    hostname: Optional[str] = None
    """The hostname of the device as reported by the agent."""

    kernel_version: Optional[str] = None
    """The operating system kernel version string reported by the agent."""

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

    os: Optional[str] = None
    """
    The operating system family the device is running, reported by the agent from
    its build-time OS vocabulary (`linux`, `windows`, or `macos`). This is the
    machine-readable OS kind, distinct from the human-readable `os_version` string.
    """

    os_version: Optional[str] = None
    """
    The human-readable long operating system version string reported by the agent
    (for example `Ubuntu 22.04` or `Windows 11 Pro`). Distinct from the
    machine-readable `os` family.
    """

    status: Literal["inactive", "activating", "online", "offline", "archived"]
    """The status of the device.

    - Inactive: The miru agent has not yet been installed / authenticated
    - Activating: The miru agent is currently being installed / authenticated
      (should only last for a few seconds)
    - Online: The miru agent has successfully pinged the server within the last 60
      seconds.
    - Offline: The miru agent has not successfully pinged the server within the last
      60 seconds (e.g. network issues, device is powered off, etc.)
    - Archived: The device has been archived. The agent's session has been revoked
      and the device no longer participates in workspace operations. See
      `archived_at` for when this occurred.
    """

    updated_at: datetime
    """Timestamp of when the device was last updated."""

    current_deployment: Optional["Deployment"] = None
    """The current deployment for the device."""

    current_release: Optional[Release] = None
    """The current release for the device."""

    group: Optional["Group"] = None
    """The group this device belongs to. Null if the device is unassigned."""


from .group import Group
from .deployment import Deployment
