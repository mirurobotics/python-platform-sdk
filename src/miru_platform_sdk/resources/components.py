# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import component_list_params, component_retrieve_params
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
from ..types.component import Component
from ..types.component_list import ComponentList

__all__ = ["ComponentsResource", "AsyncComponentsResource"]


class ComponentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ComponentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return ComponentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComponentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return ComponentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        component_id: str,
        *,
        expand: List[Literal["roles", "aspects"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Component:
        """
        Retrieve a component by ID.

        Args:
          expand: Fields to expand on the component.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not component_id:
            raise ValueError(f"Expected a non-empty value for `component_id` but received {component_id!r}")
        return self._get(
            path_template("/components/{component_id}", component_id=component_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, component_retrieve_params.ComponentRetrieveParams),
            ),
            cast_to=Component,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        device_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "roles", "aspects"]] | Omit = omit,
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
    ) -> ComponentList:
        """
        List components.

        Args:
          id: The component IDs to filter by.

          device_id: The device IDs to filter by. Returns the components these devices have reported
              a calibration for.

          expand: Fields to expand on each component in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The component names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the component results.

          slug: The component slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/components",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "device_id": device_id,
                        "expand": expand,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "slug": slug,
                    },
                    component_list_params.ComponentListParams,
                ),
            ),
            cast_to=ComponentList,
        )


class AsyncComponentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncComponentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncComponentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComponentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncComponentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        component_id: str,
        *,
        expand: List[Literal["roles", "aspects"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Component:
        """
        Retrieve a component by ID.

        Args:
          expand: Fields to expand on the component.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not component_id:
            raise ValueError(f"Expected a non-empty value for `component_id` but received {component_id!r}")
        return await self._get(
            path_template("/components/{component_id}", component_id=component_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, component_retrieve_params.ComponentRetrieveParams
                ),
            ),
            cast_to=Component,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        device_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "roles", "aspects"]] | Omit = omit,
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
    ) -> ComponentList:
        """
        List components.

        Args:
          id: The component IDs to filter by.

          device_id: The device IDs to filter by. Returns the components these devices have reported
              a calibration for.

          expand: Fields to expand on each component in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The component names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the component results.

          slug: The component slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/components",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "device_id": device_id,
                        "expand": expand,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "slug": slug,
                    },
                    component_list_params.ComponentListParams,
                ),
            ),
            cast_to=ComponentList,
        )


class ComponentsResourceWithRawResponse:
    def __init__(self, components: ComponentsResource) -> None:
        self._components = components

        self.retrieve = to_raw_response_wrapper(
            components.retrieve,
        )
        self.list = to_raw_response_wrapper(
            components.list,
        )


class AsyncComponentsResourceWithRawResponse:
    def __init__(self, components: AsyncComponentsResource) -> None:
        self._components = components

        self.retrieve = async_to_raw_response_wrapper(
            components.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            components.list,
        )


class ComponentsResourceWithStreamingResponse:
    def __init__(self, components: ComponentsResource) -> None:
        self._components = components

        self.retrieve = to_streamed_response_wrapper(
            components.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            components.list,
        )


class AsyncComponentsResourceWithStreamingResponse:
    def __init__(self, components: AsyncComponentsResource) -> None:
        self._components = components

        self.retrieve = async_to_streamed_response_wrapper(
            components.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            components.list,
        )
