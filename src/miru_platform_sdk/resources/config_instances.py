# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    config_instance_list_params,
    config_instance_create_params,
    config_instance_content_params,
    config_instance_retrieve_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.config_instance import ConfigInstance
from ..types.instance_content_param import InstanceContentParam
from ..types.config_instance_list_response import ConfigInstanceListResponse

__all__ = ["ConfigInstancesResource", "AsyncConfigInstancesResource"]


class ConfigInstancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return ConfigInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return ConfigInstancesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config_schema_id: str,
        content: InstanceContentParam,
        expand: List[Literal["content", "config_schema", "config_type"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigInstance:
        """
        Create a new config instance.

        Args:
          config_schema_id: The ID of the config schema which this config instance must adhere to.

          expand: Fields to expand on the config instance resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/config_instances",
            body=maybe_transform(
                {
                    "config_schema_id": config_schema_id,
                    "content": content,
                },
                config_instance_create_params.ConfigInstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, config_instance_create_params.ConfigInstanceCreateParams),
            ),
            cast_to=ConfigInstance,
        )

    def retrieve(
        self,
        config_instance_id: str,
        *,
        expand: List[Literal["content", "config_schema", "config_type"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigInstance:
        """
        Retrieve a config instance by ID.

        Args:
          expand: Fields to expand on the config instance resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return self._get(
            f"/config_instances/{config_instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, config_instance_retrieve_params.ConfigInstanceRetrieveParams),
            ),
            cast_to=ConfigInstance,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        config_schema_id: SequenceNotStr[str] | Omit = omit,
        config_type_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "content", "config_schema", "config_type"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigInstanceListResponse:
        """
        List config instances.

        Args:
          id: The config instance IDs to filter by.

          config_schema_id: The config schema IDs to filter by.

          config_type_id: The config type IDs to filter by.

          expand: Fields to expand on each config instance in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the config instance results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/config_instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "config_schema_id": config_schema_id,
                        "config_type_id": config_type_id,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    config_instance_list_params.ConfigInstanceListParams,
                ),
            ),
            cast_to=ConfigInstanceListResponse,
        )

    def content(
        self,
        config_instance_id: str,
        *,
        disposition: Literal["inline", "attachment"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download the content of a config instance.

        Args:
          disposition: Controls the Content-Disposition behavior. Use `inline` to display in browser or
              `attachment` to trigger a file download.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/config_instances/{config_instance_id}/content",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"disposition": disposition}, config_instance_content_params.ConfigInstanceContentParams
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncConfigInstancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncConfigInstancesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config_schema_id: str,
        content: InstanceContentParam,
        expand: List[Literal["content", "config_schema", "config_type"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigInstance:
        """
        Create a new config instance.

        Args:
          config_schema_id: The ID of the config schema which this config instance must adhere to.

          expand: Fields to expand on the config instance resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/config_instances",
            body=await async_maybe_transform(
                {
                    "config_schema_id": config_schema_id,
                    "content": content,
                },
                config_instance_create_params.ConfigInstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, config_instance_create_params.ConfigInstanceCreateParams
                ),
            ),
            cast_to=ConfigInstance,
        )

    async def retrieve(
        self,
        config_instance_id: str,
        *,
        expand: List[Literal["content", "config_schema", "config_type"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigInstance:
        """
        Retrieve a config instance by ID.

        Args:
          expand: Fields to expand on the config instance resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        return await self._get(
            f"/config_instances/{config_instance_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, config_instance_retrieve_params.ConfigInstanceRetrieveParams
                ),
            ),
            cast_to=ConfigInstance,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        config_schema_id: SequenceNotStr[str] | Omit = omit,
        config_type_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "content", "config_schema", "config_type"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigInstanceListResponse:
        """
        List config instances.

        Args:
          id: The config instance IDs to filter by.

          config_schema_id: The config schema IDs to filter by.

          config_type_id: The config type IDs to filter by.

          expand: Fields to expand on each config instance in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the config instance results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/config_instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "config_schema_id": config_schema_id,
                        "config_type_id": config_type_id,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    config_instance_list_params.ConfigInstanceListParams,
                ),
            ),
            cast_to=ConfigInstanceListResponse,
        )

    async def content(
        self,
        config_instance_id: str,
        *,
        disposition: Literal["inline", "attachment"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download the content of a config instance.

        Args:
          disposition: Controls the Content-Disposition behavior. Use `inline` to display in browser or
              `attachment` to trigger a file download.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_instance_id:
            raise ValueError(f"Expected a non-empty value for `config_instance_id` but received {config_instance_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/config_instances/{config_instance_id}/content",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"disposition": disposition}, config_instance_content_params.ConfigInstanceContentParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ConfigInstancesResourceWithRawResponse:
    def __init__(self, config_instances: ConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.create = to_raw_response_wrapper(
            config_instances.create,
        )
        self.retrieve = to_raw_response_wrapper(
            config_instances.retrieve,
        )
        self.list = to_raw_response_wrapper(
            config_instances.list,
        )
        self.content = to_custom_raw_response_wrapper(
            config_instances.content,
            BinaryAPIResponse,
        )


class AsyncConfigInstancesResourceWithRawResponse:
    def __init__(self, config_instances: AsyncConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.create = async_to_raw_response_wrapper(
            config_instances.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            config_instances.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            config_instances.list,
        )
        self.content = async_to_custom_raw_response_wrapper(
            config_instances.content,
            AsyncBinaryAPIResponse,
        )


class ConfigInstancesResourceWithStreamingResponse:
    def __init__(self, config_instances: ConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.create = to_streamed_response_wrapper(
            config_instances.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            config_instances.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            config_instances.list,
        )
        self.content = to_custom_streamed_response_wrapper(
            config_instances.content,
            StreamedBinaryAPIResponse,
        )


class AsyncConfigInstancesResourceWithStreamingResponse:
    def __init__(self, config_instances: AsyncConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.create = async_to_streamed_response_wrapper(
            config_instances.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            config_instances.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            config_instances.list,
        )
        self.content = async_to_custom_streamed_response_wrapper(
            config_instances.content,
            AsyncStreamedBinaryAPIResponse,
        )
