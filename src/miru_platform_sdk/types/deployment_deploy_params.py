# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DeploymentDeployParams"]


class DeploymentDeployParams(TypedDict, total=False):
    expand: List[Literal["device", "release", "parent", "config_instances", "created_by", "updated_by", "queued_by"]]
    """Fields to expand on the deployment resource."""
