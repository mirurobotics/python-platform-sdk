# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import config_schema_list_params, config_schema_create_params, config_schema_retrieve_params
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
from ..types.config_schema import ConfigSchema
from ..types.config_schema_list import ConfigSchemaList

__all__ = ["ConfigSchemasResource", "AsyncConfigSchemasResource"]


class ConfigSchemasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-platform-python#accessing-raw-response-data-eg-headers
        """
        return ConfigSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-platform-python#with_streaming_response
        """
        return ConfigSchemasResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config_type_ref: config_schema_create_params.ConfigTypeRef,
        documents: Iterable[config_schema_create_params.Document],
        format: Literal["json", "yaml", "cue"],
        language: Literal["jsonschema", "cue"],
        miru_version: str,
        expand: List[Literal["documents", "config_type"]] | Omit = omit,
        git_commit: config_schema_create_params.GitCommit | Omit = omit,
        instance_filepath: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigSchema:
        """
        Create a new config schema.

        Args:
          config_type_ref: A reference to a config type. At least one of `id` or `slug` must be provided.
              When both are provided, `id` takes precedence and `slug` is ignored.

          documents: The schema document files.

          expand: Fields to expand on the config schema resource.

          git_commit: The git commit to link to this config schema.

          instance_filepath: The file path for config instances created from this schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Miru-Version": miru_version, **(extra_headers or {})}
        return self._post(
            "/config_schemas",
            body=maybe_transform(
                {
                    "config_type_ref": config_type_ref,
                    "documents": documents,
                    "format": format,
                    "language": language,
                    "git_commit": git_commit,
                    "instance_filepath": instance_filepath,
                },
                config_schema_create_params.ConfigSchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, config_schema_create_params.ConfigSchemaCreateParams),
            ),
            cast_to=ConfigSchema,
        )

    def retrieve(
        self,
        config_schema_id: str,
        *,
        miru_version: str,
        expand: List[Literal["documents", "config_type"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigSchema:
        """
        Retrieve a config schema by ID.

        Args:
          expand: Fields to expand on the config schema resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_schema_id:
            raise ValueError(f"Expected a non-empty value for `config_schema_id` but received {config_schema_id!r}")
        extra_headers = {"Miru-Version": miru_version, **(extra_headers or {})}
        return self._get(
            f"/config_schemas/{config_schema_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, config_schema_retrieve_params.ConfigSchemaRetrieveParams),
            ),
            cast_to=ConfigSchema,
        )

    def list(
        self,
        *,
        miru_version: str,
        id: SequenceNotStr[str] | Omit = omit,
        config_type_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "documents", "config_type"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigSchemaList:
        """
        List config schemas.

        Args:
          id: The config schema IDs to filter by.

          config_type_id: The config type IDs to filter by.

          expand: Fields to expand on each config schema in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the config schema results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Miru-Version": miru_version, **(extra_headers or {})}
        return self._get(
            "/config_schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "config_type_id": config_type_id,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    config_schema_list_params.ConfigSchemaListParams,
                ),
            ),
            cast_to=ConfigSchemaList,
        )


class AsyncConfigSchemasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-platform-python#with_streaming_response
        """
        return AsyncConfigSchemasResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config_type_ref: config_schema_create_params.ConfigTypeRef,
        documents: Iterable[config_schema_create_params.Document],
        format: Literal["json", "yaml", "cue"],
        language: Literal["jsonschema", "cue"],
        miru_version: str,
        expand: List[Literal["documents", "config_type"]] | Omit = omit,
        git_commit: config_schema_create_params.GitCommit | Omit = omit,
        instance_filepath: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigSchema:
        """
        Create a new config schema.

        Args:
          config_type_ref: A reference to a config type. At least one of `id` or `slug` must be provided.
              When both are provided, `id` takes precedence and `slug` is ignored.

          documents: The schema document files.

          expand: Fields to expand on the config schema resource.

          git_commit: The git commit to link to this config schema.

          instance_filepath: The file path for config instances created from this schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Miru-Version": miru_version, **(extra_headers or {})}
        return await self._post(
            "/config_schemas",
            body=await async_maybe_transform(
                {
                    "config_type_ref": config_type_ref,
                    "documents": documents,
                    "format": format,
                    "language": language,
                    "git_commit": git_commit,
                    "instance_filepath": instance_filepath,
                },
                config_schema_create_params.ConfigSchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, config_schema_create_params.ConfigSchemaCreateParams
                ),
            ),
            cast_to=ConfigSchema,
        )

    async def retrieve(
        self,
        config_schema_id: str,
        *,
        miru_version: str,
        expand: List[Literal["documents", "config_type"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigSchema:
        """
        Retrieve a config schema by ID.

        Args:
          expand: Fields to expand on the config schema resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_schema_id:
            raise ValueError(f"Expected a non-empty value for `config_schema_id` but received {config_schema_id!r}")
        extra_headers = {"Miru-Version": miru_version, **(extra_headers or {})}
        return await self._get(
            f"/config_schemas/{config_schema_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, config_schema_retrieve_params.ConfigSchemaRetrieveParams
                ),
            ),
            cast_to=ConfigSchema,
        )

    async def list(
        self,
        *,
        miru_version: str,
        id: SequenceNotStr[str] | Omit = omit,
        config_type_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "documents", "config_type"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigSchemaList:
        """
        List config schemas.

        Args:
          id: The config schema IDs to filter by.

          config_type_id: The config type IDs to filter by.

          expand: Fields to expand on each config schema in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the config schema results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Miru-Version": miru_version, **(extra_headers or {})}
        return await self._get(
            "/config_schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "config_type_id": config_type_id,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    config_schema_list_params.ConfigSchemaListParams,
                ),
            ),
            cast_to=ConfigSchemaList,
        )


class ConfigSchemasResourceWithRawResponse:
    def __init__(self, config_schemas: ConfigSchemasResource) -> None:
        self._config_schemas = config_schemas

        self.create = to_raw_response_wrapper(
            config_schemas.create,
        )
        self.retrieve = to_raw_response_wrapper(
            config_schemas.retrieve,
        )
        self.list = to_raw_response_wrapper(
            config_schemas.list,
        )


class AsyncConfigSchemasResourceWithRawResponse:
    def __init__(self, config_schemas: AsyncConfigSchemasResource) -> None:
        self._config_schemas = config_schemas

        self.create = async_to_raw_response_wrapper(
            config_schemas.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            config_schemas.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            config_schemas.list,
        )


class ConfigSchemasResourceWithStreamingResponse:
    def __init__(self, config_schemas: ConfigSchemasResource) -> None:
        self._config_schemas = config_schemas

        self.create = to_streamed_response_wrapper(
            config_schemas.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            config_schemas.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            config_schemas.list,
        )


class AsyncConfigSchemasResourceWithStreamingResponse:
    def __init__(self, config_schemas: AsyncConfigSchemasResource) -> None:
        self._config_schemas = config_schemas

        self.create = async_to_streamed_response_wrapper(
            config_schemas.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            config_schemas.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            config_schemas.list,
        )
