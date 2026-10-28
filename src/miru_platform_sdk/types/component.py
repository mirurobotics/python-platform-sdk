# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Component"]


class Component(BaseModel):
    """
    A kind of hardware on a device whose calibrations Miru stores, such as an arm or a camera. Miru creates a component the first time a device reports a calibration with a new slug; components are never created, archived, or deleted through the API. A workspace holds at most 100 components.
    """

    id: str
    """ID of the component."""

    created_at: datetime
    """
    Timestamp of when Miru created the component, which is when a device first
    reported a calibration with its slug.
    """

    name: str
    """Display name of the component.

    Defaults to a name inferred from the slug, with words split on `-` and `_` and
    each capitalized (`front-camera` becomes `Front Camera`). Publishers can rename
    it.
    """

    object: Literal["component"]
    """The object type, which is always `component`."""

    slug: str
    """
    An immutable, code-friendly name for the component, validated like config type
    slugs. Component slugs and config type slugs are separate namespaces, so a
    component may share a slug with a config type.
    """

    updated_at: datetime
    """Timestamp of when the component was last updated."""

    aspects: Optional[List["ComponentAspect"]] = None
    """The component's aspects, in the order first reported.

    Miru adds an aspect the first time a device reports it and never removes one. At
    most 100. Expand using `expand=aspects` in the query string.
    """

    roles: Optional[List["ComponentRole"]] = None
    """The component's roles, in the order first reported.

    Miru adds a role the first time a device reports it and never removes one. At
    most 100. Expand using `expand=roles` in the query string.
    """


from .component_role import ComponentRole
from .component_aspect import ComponentAspect
