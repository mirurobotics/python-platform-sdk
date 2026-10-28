# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import component_aspect_list_params, component_aspect_retrieve_params
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
from ..types.component_aspect import ComponentAspect
from ..types.component_aspect_list import ComponentAspectList

__all__ = ["ComponentAspectsResource", "AsyncComponentAspectsResource"]


class ComponentAspectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ComponentAspectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return ComponentAspectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComponentAspectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return ComponentAspectsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        component_aspect_id: str,
        *,
        expand: List[Literal["component"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComponentAspect:
        """
        Retrieve a component aspect by ID.

        Args:
          expand: Fields to expand on the component aspect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not component_aspect_id:
            raise ValueError(
                f"Expected a non-empty value for `component_aspect_id` but received {component_aspect_id!r}"
            )
        return self._get(
            path_template("/component_aspects/{component_aspect_id}", component_aspect_id=component_aspect_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"expand": expand}, component_aspect_retrieve_params.ComponentAspectRetrieveParams
                ),
            ),
            cast_to=ComponentAspect,
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
    ) -> ComponentAspectList:
        """
        List component aspects, oldest first by default.

        Args:
          id: The component aspect IDs to filter by.

          component_id: The component IDs to filter by.

          expand: Fields to expand on each component aspect in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The component aspect names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the component aspect results.

          slug: The component aspect slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/component_aspects",
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
                    component_aspect_list_params.ComponentAspectListParams,
                ),
            ),
            cast_to=ComponentAspectList,
        )


class AsyncComponentAspectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncComponentAspectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncComponentAspectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComponentAspectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncComponentAspectsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        component_aspect_id: str,
        *,
        expand: List[Literal["component"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComponentAspect:
        """
        Retrieve a component aspect by ID.

        Args:
          expand: Fields to expand on the component aspect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not component_aspect_id:
            raise ValueError(
                f"Expected a non-empty value for `component_aspect_id` but received {component_aspect_id!r}"
            )
        return await self._get(
            path_template("/component_aspects/{component_aspect_id}", component_aspect_id=component_aspect_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, component_aspect_retrieve_params.ComponentAspectRetrieveParams
                ),
            ),
            cast_to=ComponentAspect,
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
    ) -> ComponentAspectList:
        """
        List component aspects, oldest first by default.

        Args:
          id: The component aspect IDs to filter by.

          component_id: The component IDs to filter by.

          expand: Fields to expand on each component aspect in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The component aspect names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the component aspect results.

          slug: The component aspect slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/component_aspects",
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
                    component_aspect_list_params.ComponentAspectListParams,
                ),
            ),
            cast_to=ComponentAspectList,
        )


class ComponentAspectsResourceWithRawResponse:
    def __init__(self, component_aspects: ComponentAspectsResource) -> None:
        self._component_aspects = component_aspects

        self.retrieve = to_raw_response_wrapper(
            component_aspects.retrieve,
        )
        self.list = to_raw_response_wrapper(
            component_aspects.list,
        )


class AsyncComponentAspectsResourceWithRawResponse:
    def __init__(self, component_aspects: AsyncComponentAspectsResource) -> None:
        self._component_aspects = component_aspects

        self.retrieve = async_to_raw_response_wrapper(
            component_aspects.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            component_aspects.list,
        )


class ComponentAspectsResourceWithStreamingResponse:
    def __init__(self, component_aspects: ComponentAspectsResource) -> None:
        self._component_aspects = component_aspects

        self.retrieve = to_streamed_response_wrapper(
            component_aspects.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            component_aspects.list,
        )


class AsyncComponentAspectsResourceWithStreamingResponse:
    def __init__(self, component_aspects: AsyncComponentAspectsResource) -> None:
        self._component_aspects = component_aspects

        self.retrieve = async_to_streamed_response_wrapper(
            component_aspects.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            component_aspects.list,
        )
