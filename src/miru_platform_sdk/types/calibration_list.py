# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .calibration import Calibration
from .shared.paginated_list import PaginatedList

__all__ = ["CalibrationList"]


class CalibrationList(PaginatedList):
    data: List[Calibration]
    """The list of calibrations."""
