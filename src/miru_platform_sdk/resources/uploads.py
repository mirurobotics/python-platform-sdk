# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import upload_list_params
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
from ..types.upload import Upload
from ..types.upload_list import UploadList
from ..types.upload_status import UploadStatus

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """
        Retrieve an upload by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return self._get(
            path_template("/uploads/{upload_id}", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Upload,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        bundle_id: SequenceNotStr[str] | Omit = omit,
        device_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        file_rule_id: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[
            Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc", "uploaded_at:asc", "uploaded_at:desc"]
        ]
        | Omit = omit,
        status: List[UploadStatus] | Omit = omit,
        upload_collection_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadList:
        """
        List uploads.

        Args:
          id: The upload IDs to filter by.

          bundle_id: The upload bundle IDs to filter by.

          device_id: The device IDs to filter by.

          expand: Fields to expand on each upload in the list.

          file_rule_id: The file rule IDs to filter by.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the upload results.

          status: The upload statuses to filter by.

          upload_collection_id: The upload collection IDs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/uploads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "bundle_id": bundle_id,
                        "device_id": device_id,
                        "expand": expand,
                        "file_rule_id": file_rule_id,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "status": status,
                        "upload_collection_id": upload_collection_id,
                    },
                    upload_list_params.UploadListParams,
                ),
            ),
            cast_to=UploadList,
        )


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """
        Retrieve an upload by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return await self._get(
            path_template("/uploads/{upload_id}", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Upload,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        bundle_id: SequenceNotStr[str] | Omit = omit,
        device_id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        file_rule_id: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[
            Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc", "uploaded_at:asc", "uploaded_at:desc"]
        ]
        | Omit = omit,
        status: List[UploadStatus] | Omit = omit,
        upload_collection_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadList:
        """
        List uploads.

        Args:
          id: The upload IDs to filter by.

          bundle_id: The upload bundle IDs to filter by.

          device_id: The device IDs to filter by.

          expand: Fields to expand on each upload in the list.

          file_rule_id: The file rule IDs to filter by.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the upload results.

          status: The upload statuses to filter by.

          upload_collection_id: The upload collection IDs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/uploads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "bundle_id": bundle_id,
                        "device_id": device_id,
                        "expand": expand,
                        "file_rule_id": file_rule_id,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "status": status,
                        "upload_collection_id": upload_collection_id,
                    },
                    upload_list_params.UploadListParams,
                ),
            ),
            cast_to=UploadList,
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.retrieve = to_raw_response_wrapper(
            uploads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            uploads.list,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.retrieve = async_to_raw_response_wrapper(
            uploads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            uploads.list,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.retrieve = to_streamed_response_wrapper(
            uploads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            uploads.list,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.retrieve = async_to_streamed_response_wrapper(
            uploads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            uploads.list,
        )
