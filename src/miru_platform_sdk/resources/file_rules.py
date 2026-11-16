# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import file_rule_list_params
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
from ..types.file_rule import FileRule
from ..types.file_rule_list import FileRuleList

__all__ = ["FileRulesResource", "AsyncFileRulesResource"]


class FileRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return FileRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return FileRulesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        file_rule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRule:
        """
        Retrieve a file rule by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_rule_id:
            raise ValueError(f"Expected a non-empty value for `file_rule_id` but received {file_rule_id!r}")
        return self._get(
            path_template("/file_rules/{file_rule_id}", file_rule_id=file_rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRule,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        bucket: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc"]] | Omit = omit,
        upload_collection_id: SequenceNotStr[str] | Omit = omit,
        upload_collection_slug: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRuleList:
        """
        List file rules.

        Args:
          id: The file rule IDs to filter by.

          bucket: The upload bucket names to filter by. A retention-only file rule, which has no
              `upload` block, never matches this filter.

          expand: Fields to expand on each file rule in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the file rule results.

          upload_collection_id: The upload collection IDs to filter by. A retention-only file rule, which has no
              `upload` block, never matches this filter.

          upload_collection_slug: The upload collection slugs to filter by. A retention-only file rule, which has
              no `upload` block, never matches this filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/file_rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "bucket": bucket,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "upload_collection_id": upload_collection_id,
                        "upload_collection_slug": upload_collection_slug,
                    },
                    file_rule_list_params.FileRuleListParams,
                ),
            ),
            cast_to=FileRuleList,
        )


class AsyncFileRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFileRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncFileRulesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        file_rule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRule:
        """
        Retrieve a file rule by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_rule_id:
            raise ValueError(f"Expected a non-empty value for `file_rule_id` but received {file_rule_id!r}")
        return await self._get(
            path_template("/file_rules/{file_rule_id}", file_rule_id=file_rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRule,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        bucket: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc"]] | Omit = omit,
        upload_collection_id: SequenceNotStr[str] | Omit = omit,
        upload_collection_slug: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRuleList:
        """
        List file rules.

        Args:
          id: The file rule IDs to filter by.

          bucket: The upload bucket names to filter by. A retention-only file rule, which has no
              `upload` block, never matches this filter.

          expand: Fields to expand on each file rule in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the file rule results.

          upload_collection_id: The upload collection IDs to filter by. A retention-only file rule, which has no
              `upload` block, never matches this filter.

          upload_collection_slug: The upload collection slugs to filter by. A retention-only file rule, which has
              no `upload` block, never matches this filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/file_rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "bucket": bucket,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "upload_collection_id": upload_collection_id,
                        "upload_collection_slug": upload_collection_slug,
                    },
                    file_rule_list_params.FileRuleListParams,
                ),
            ),
            cast_to=FileRuleList,
        )


class FileRulesResourceWithRawResponse:
    def __init__(self, file_rules: FileRulesResource) -> None:
        self._file_rules = file_rules

        self.retrieve = to_raw_response_wrapper(
            file_rules.retrieve,
        )
        self.list = to_raw_response_wrapper(
            file_rules.list,
        )


class AsyncFileRulesResourceWithRawResponse:
    def __init__(self, file_rules: AsyncFileRulesResource) -> None:
        self._file_rules = file_rules

        self.retrieve = async_to_raw_response_wrapper(
            file_rules.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            file_rules.list,
        )


class FileRulesResourceWithStreamingResponse:
    def __init__(self, file_rules: FileRulesResource) -> None:
        self._file_rules = file_rules

        self.retrieve = to_streamed_response_wrapper(
            file_rules.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            file_rules.list,
        )


class AsyncFileRulesResourceWithStreamingResponse:
    def __init__(self, file_rules: AsyncFileRulesResource) -> None:
        self._file_rules = file_rules

        self.retrieve = async_to_streamed_response_wrapper(
            file_rules.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            file_rules.list,
        )
