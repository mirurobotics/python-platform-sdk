# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    config_instance_ids: Required[SequenceNotStr[str]]
    """The IDs of the config instances to deploy.

    A deployment must include config instances according to the config schemas slots
    defined in the release.
    """

    description: Required[str]
    """The description of the deployment."""

    device_id: Required[str]
    """The ID of the device that the deployment is being created for."""

    release_id: Required[str]
    """The release ID which this deployment adheres to."""

    target_status: Required[Literal["staged", "deployed"]]
    """Desired state of the deployment.

    `staged` means the deployment is ready for deployment. Deployments can only be
    staged if their release is not the device's current release.

    `deployed` means the deployment should be deployed to the device. Deployments
    can only be deployed if their release is the device's current release.
    """

    expand: List[Literal["device", "release", "config_instances"]]
    """Fields to expand on the deployment resource."""

    parent_id: Optional[str]
    """Parent deployment ID used as an optimistic-concurrency token. Tristate:

    - omitted: server fills with the device's current `target_deployment_id`; no
      concurrency check.
    - null: caller asserts the device has no current target; 409 if it does.
    - value: caller asserts the device's current target equals this ID; 409 if it
      does not match.
    """
