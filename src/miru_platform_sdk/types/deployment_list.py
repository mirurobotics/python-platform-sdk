# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .shared.paginated_list import PaginatedList

__all__ = ["DeploymentList"]


class DeploymentList(PaginatedList):
    data: List["Deployment"]
    """The list of deployments."""


from .deployment import Deployment
