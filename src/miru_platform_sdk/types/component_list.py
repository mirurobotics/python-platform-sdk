# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .shared.paginated_list import PaginatedList

__all__ = ["ComponentList"]


class ComponentList(PaginatedList):
    data: List["Component"]
    """The list of components."""


from .component import Component
