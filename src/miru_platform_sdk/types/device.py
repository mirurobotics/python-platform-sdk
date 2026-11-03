# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .release import Release
from .._models import BaseModel
from .principal import Principal

__all__ = ["Device"]


class Device(BaseModel):
    id: str
    """ID of the device."""

    agent_version: Optional[str] = None
    """The version of the agent the device is running."""

    arch: Optional[Literal["x86_64", "aarch64"]] = None
    """A CPU architecture, from the agent's build-time architecture vocabulary.

    Shared across resources (devices, config schemas, file rules). These are the
    canonical wire values.

    - `x86_64`
    - `aarch64`
    """

    archived_at: Optional[datetime] = None
    """Timestamp of when the device was archived. Null if the device is not archived."""

    archived_by_id: Optional[str] = None
    """ID of the principal who archived the device.

    Null if the device is not archived or was archived before this field was
    recorded.
    """

    created_at: datetime
    """Timestamp of when the device was created."""

    created_by_id: str
    """ID of the principal who created the device."""

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

    os: Optional[Literal["linux", "windows"]] = None
    """An operating system family, from the agent's build-time OS vocabulary.

    Shared across resources (devices, config schemas, file rules, releases). This is
    the machine-readable OS kind, distinct from a human-readable version string.

    - `linux`
    - `windows`
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

    updated_by_id: str
    """ID of the principal who last updated the device."""

    archived_by: Optional[Principal] = None
    """The principal who archived the device.

    Null if `archived_by_id` is null. Expand using `expand=archived_by` in the query
    string.
    """

    created_by: Optional[Principal] = None
    """The principal who created the device.

    Expand using `expand=created_by` in the query string.
    """

    current_deployment: Optional["Deployment"] = None
    """The current deployment for the device."""

    current_release: Optional[Release] = None
    """The current release for the device."""

    group: Optional["Group"] = None
    """The group this device belongs to. Null if the device is unassigned."""

    updated_by: Optional[Principal] = None
    """The principal who last updated the device.

    Expand using `expand=updated_by` in the query string.
    """


from .group import Group
from .deployment import Deployment
