# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    config_instance_ids: Required[SequenceNotStr[str]]
    """The IDs of the config instances to deploy.

    A deployment must have exactly one config instance for each config schema in the
    deployment's release.
    """

    description: Required[str]
    """The description of the deployment."""

    device_id: Required[str]
    """The ID of the device that the deployment is being created for."""

    release_id: Required[str]
    """The release ID which this deployment adheres to."""

    target_status: Required[Literal["staged", "deployed"]]
    """Desired state of the deployment.

    - Staged: ready for deployment. Deployments can only be staged if their release
      is not the current release for the device.
    - Deployed: deployed to the device. Deployments can only be deployed if their
      release is the device's current release.
    """

    expand: List[Literal["device", "release", "config_instances"]]
    """Fields to expand on the deployment resource."""

    parent_id: str
    """The ID of the deployment that this deployment was patched from."""
