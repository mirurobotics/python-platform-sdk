# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SchemaDocument"]


class SchemaDocument(BaseModel):
    id: str
    """The unique identifier for this document."""

    data: str
    """The raw document content."""

    name: str
    """The identifier for this document."""
