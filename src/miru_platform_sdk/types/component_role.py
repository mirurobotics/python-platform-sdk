# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ComponentRole"]


class ComponentRole(BaseModel):
    """A role a calibrated unit fills on a device, such as `left` or `front-left`.

    Miru creates a role the first time a device reports a calibration with a new role for the component; roles are never created or deleted through the API. A component holds at most 100 roles.
    """

    id: str
    """ID of the role."""

    component_id: str
    """ID of the component the role belongs to."""

    created_at: datetime
    """
    Timestamp of when Miru created the role, which is when a device first reported a
    calibration with its slug for the component.
    """

    name: str
    """Display name of the role.

    Defaults to a name inferred from the slug, with words split on `-` and `_` and
    each capitalized (`front-left` becomes `Front Left`). Publishers can rename it.
    """

    object: Literal["component_role"]
    """The object type, which is always `component_role`."""

    slug: str
    """
    The immutable value devices report as `role` when they create a calibration,
    unique within the component.
    """

    updated_at: datetime
    """Timestamp of when the role was last updated."""

    component: Optional["Component"] = None
    """
    A kind of hardware on a device whose calibrations Miru stores, such as an arm or
    a camera. Miru creates a component the first time a device reports a calibration
    with a new slug; components are never created, archived, or deleted through the
    API. A workspace holds at most 100 components.
    """


from .component import Component
