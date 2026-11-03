# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .user import User
from .shared.paginated_list import PaginatedList

__all__ = ["UserList"]


class UserList(PaginatedList):
    data: List[User]
    """The list of users."""
