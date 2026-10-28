# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import component_role_list_params, component_role_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.component_role import ComponentRole
from ..types.component_role_list import ComponentRoleList

__all__ = ["ComponentRolesResource", "AsyncComponentRolesResource"]


class ComponentRolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ComponentRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return ComponentRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComponentRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return ComponentRolesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        component_role_id: str,
        *,
        expand: List[Literal["component"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComponentRole:
        """
        Retrieve a component role by ID.

        Args:
          expand: Fields to expand on the component role.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not component_role_id:
            raise ValueError(f"Expected a non-empty value for `component_role_id` but received {component_role_id!r}")
        return self._get(
            path_template("/component_roles/{component_role_id}", component_role_id=component_role_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, component_role_retrieve_params.ComponentRoleRetrieveParams),
            ),
            cast_to=ComponentRole,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        component_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "component"]] | Omit = omit,
        limit: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[
            Literal[
                "id:asc",
                "id:desc",
                "created_at:asc",
                "created_at:desc",
                "updated_at:asc",
                "updated_at:desc",
                "name:asc",
                "name:desc",
                "slug:asc",
                "slug:desc",
            ]
        ]
        | Omit = omit,
        slug: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComponentRoleList:
        """
        List component roles, oldest first by default.

        Args:
          id: The component role IDs to filter by.

          component_id: The component IDs to filter by.

          expand: Fields to expand on each component role in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The component role names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the component role results.

          slug: The component role slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/component_roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "component_id": component_id,
                        "expand": expand,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "slug": slug,
                    },
                    component_role_list_params.ComponentRoleListParams,
                ),
            ),
            cast_to=ComponentRoleList,
        )


class AsyncComponentRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncComponentRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncComponentRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComponentRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncComponentRolesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        component_role_id: str,
        *,
        expand: List[Literal["component"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComponentRole:
        """
        Retrieve a component role by ID.

        Args:
          expand: Fields to expand on the component role.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not component_role_id:
            raise ValueError(f"Expected a non-empty value for `component_role_id` but received {component_role_id!r}")
        return await self._get(
            path_template("/component_roles/{component_role_id}", component_role_id=component_role_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, component_role_retrieve_params.ComponentRoleRetrieveParams
                ),
            ),
            cast_to=ComponentRole,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        component_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "component"]] | Omit = omit,
        limit: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[
            Literal[
                "id:asc",
                "id:desc",
                "created_at:asc",
                "created_at:desc",
                "updated_at:asc",
                "updated_at:desc",
                "name:asc",
                "name:desc",
                "slug:asc",
                "slug:desc",
            ]
        ]
        | Omit = omit,
        slug: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComponentRoleList:
        """
        List component roles, oldest first by default.

        Args:
          id: The component role IDs to filter by.

          component_id: The component IDs to filter by.

          expand: Fields to expand on each component role in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The component role names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the component role results.

          slug: The component role slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/component_roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "component_id": component_id,
                        "expand": expand,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "slug": slug,
                    },
                    component_role_list_params.ComponentRoleListParams,
                ),
            ),
            cast_to=ComponentRoleList,
        )


class ComponentRolesResourceWithRawResponse:
    def __init__(self, component_roles: ComponentRolesResource) -> None:
        self._component_roles = component_roles

        self.retrieve = to_raw_response_wrapper(
            component_roles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            component_roles.list,
        )


class AsyncComponentRolesResourceWithRawResponse:
    def __init__(self, component_roles: AsyncComponentRolesResource) -> None:
        self._component_roles = component_roles

        self.retrieve = async_to_raw_response_wrapper(
            component_roles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            component_roles.list,
        )


class ComponentRolesResourceWithStreamingResponse:
    def __init__(self, component_roles: ComponentRolesResource) -> None:
        self._component_roles = component_roles

        self.retrieve = to_streamed_response_wrapper(
            component_roles.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            component_roles.list,
        )


class AsyncComponentRolesResourceWithStreamingResponse:
    def __init__(self, component_roles: AsyncComponentRolesResource) -> None:
        self._component_roles = component_roles

        self.retrieve = async_to_streamed_response_wrapper(
            component_roles.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            component_roles.list,
        )
