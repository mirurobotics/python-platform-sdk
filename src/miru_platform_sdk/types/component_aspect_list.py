# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .shared.paginated_list import PaginatedList

__all__ = ["ComponentAspectList"]


class ComponentAspectList(PaginatedList):
    data: List["ComponentAspect"]
    """The list of component aspects."""


from .component_aspect import ComponentAspect
