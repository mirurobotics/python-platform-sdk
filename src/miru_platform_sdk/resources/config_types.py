# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import config_type_list_params, config_type_create_params, config_type_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.config_type import ConfigType
from ..types.config_type_list_response import ConfigTypeListResponse

__all__ = ["ConfigTypesResource", "AsyncConfigTypesResource"]


class ConfigTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return ConfigTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return ConfigTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigType:
        """
        Create a new config type.

        Args:
          name: The name of the config type.

          slug: An immutable, code-friendly name for the config type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/config_types",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                config_type_create_params.ConfigTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigType,
        )

    def retrieve(
        self,
        config_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigType:
        """
        Retrieve a config type by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_type_id:
            raise ValueError(f"Expected a non-empty value for `config_type_id` but received {config_type_id!r}")
        return self._get(
            f"/config_types/{config_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigType,
        )

    def update(
        self,
        config_type_id: str,
        *,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigType:
        """
        Update a config type by ID.

        Args:
          name: The updated name of the config type.

          slug: The updated slug for the config type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_type_id:
            raise ValueError(f"Expected a non-empty value for `config_type_id` but received {config_type_id!r}")
        return self._patch(
            f"/config_types/{config_type_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                config_type_update_params.ConfigTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigType,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        slug: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigTypeListResponse:
        """
        List config types.

        Args:
          id: The config type IDs to filter by.

          expand: Fields to expand on each config type in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The config type names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the config type results.

          slug: The config type slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/config_types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "expand": expand,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "slug": slug,
                    },
                    config_type_list_params.ConfigTypeListParams,
                ),
            ),
            cast_to=ConfigTypeListResponse,
        )


class AsyncConfigTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncConfigTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigType:
        """
        Create a new config type.

        Args:
          name: The name of the config type.

          slug: An immutable, code-friendly name for the config type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/config_types",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                config_type_create_params.ConfigTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigType,
        )

    async def retrieve(
        self,
        config_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigType:
        """
        Retrieve a config type by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_type_id:
            raise ValueError(f"Expected a non-empty value for `config_type_id` but received {config_type_id!r}")
        return await self._get(
            f"/config_types/{config_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigType,
        )

    async def update(
        self,
        config_type_id: str,
        *,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigType:
        """
        Update a config type by ID.

        Args:
          name: The updated name of the config type.

          slug: The updated slug for the config type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_type_id:
            raise ValueError(f"Expected a non-empty value for `config_type_id` but received {config_type_id!r}")
        return await self._patch(
            f"/config_types/{config_type_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                config_type_update_params.ConfigTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigType,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        slug: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigTypeListResponse:
        """
        List config types.

        Args:
          id: The config type IDs to filter by.

          expand: Fields to expand on each config type in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The config type names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the config type results.

          slug: The config type slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/config_types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "expand": expand,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "slug": slug,
                    },
                    config_type_list_params.ConfigTypeListParams,
                ),
            ),
            cast_to=ConfigTypeListResponse,
        )


class ConfigTypesResourceWithRawResponse:
    def __init__(self, config_types: ConfigTypesResource) -> None:
        self._config_types = config_types

        self.create = to_raw_response_wrapper(
            config_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            config_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            config_types.update,
        )
        self.list = to_raw_response_wrapper(
            config_types.list,
        )


class AsyncConfigTypesResourceWithRawResponse:
    def __init__(self, config_types: AsyncConfigTypesResource) -> None:
        self._config_types = config_types

        self.create = async_to_raw_response_wrapper(
            config_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            config_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            config_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            config_types.list,
        )


class ConfigTypesResourceWithStreamingResponse:
    def __init__(self, config_types: ConfigTypesResource) -> None:
        self._config_types = config_types

        self.create = to_streamed_response_wrapper(
            config_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            config_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            config_types.update,
        )
        self.list = to_streamed_response_wrapper(
            config_types.list,
        )


class AsyncConfigTypesResourceWithStreamingResponse:
    def __init__(self, config_types: AsyncConfigTypesResource) -> None:
        self._config_types = config_types

        self.create = async_to_streamed_response_wrapper(
            config_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            config_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            config_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            config_types.list,
        )
