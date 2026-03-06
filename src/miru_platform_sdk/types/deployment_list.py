# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .deployment import Deployment
from .shared.paginated_list import PaginatedList

__all__ = ["DeploymentList"]


class DeploymentList(PaginatedList):
    data: List[Deployment]
    """The list of deployments."""
