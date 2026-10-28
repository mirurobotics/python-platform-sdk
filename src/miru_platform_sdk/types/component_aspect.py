# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ComponentAspect"]


class ComponentAspect(BaseModel):
    """
    An aspect of a unit that was calibrated, when the unit has more than one, such as `pose` or `joint-offsets`. Miru creates an aspect the first time a device reports a calibration with a new aspect for the component; aspects are never created or deleted through the API. A component holds at most 100 aspects.
    """

    id: str
    """ID of the aspect."""

    component_id: str
    """ID of the component the aspect belongs to."""

    created_at: datetime
    """
    Timestamp of when Miru created the aspect, which is when a device first reported
    a calibration with its slug for the component.
    """

    name: str
    """Display name of the aspect.

    Defaults to a name inferred from the slug, with words split on `-` and `_` and
    each capitalized (`joint-offsets` becomes `Joint Offsets`). Publishers can
    rename it.
    """

    object: Literal["component_aspect"]
    """The object type, which is always `component_aspect`."""

    slug: str
    """
    The immutable value devices report as `aspect` when they create a calibration,
    unique within the component.
    """

    updated_at: datetime
    """Timestamp of when the aspect was last updated."""

    component: Optional["Component"] = None
    """
    A kind of hardware on a device whose calibrations Miru stores, such as an arm or
    a camera. Miru creates a component the first time a device reports a calibration
    with a new slug; components are never created, archived, or deleted through the
    API. A workspace holds at most 100 components.
    """


from .component import Component
