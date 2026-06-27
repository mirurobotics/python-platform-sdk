# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import upload_collection_list_params, upload_collection_create_params, upload_collection_update_params
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
from ..types.upload_collection import UploadCollection
from ..types.upload_collection_list_response import UploadCollectionListResponse

__all__ = ["UploadCollectionsResource", "AsyncUploadCollectionsResource"]


class UploadCollectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return UploadCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return UploadCollectionsResourceWithStreamingResponse(self)

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
    ) -> UploadCollection:
        """
        Create a new upload collection.

        Args:
          name: The name of the upload collection.

          slug: An immutable, code-friendly name for the upload collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/upload_collections",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                upload_collection_create_params.UploadCollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCollection,
        )

    def retrieve(
        self,
        upload_collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCollection:
        """
        Retrieve an upload collection by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_collection_id:
            raise ValueError(
                f"Expected a non-empty value for `upload_collection_id` but received {upload_collection_id!r}"
            )
        return self._get(
            path_template("/upload_collections/{upload_collection_id}", upload_collection_id=upload_collection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCollection,
        )

    def update(
        self,
        upload_collection_id: str,
        *,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCollection:
        """
        Update an upload collection by ID.

        Args:
          name: The updated name of the upload collection.

          slug: The updated slug for the upload collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_collection_id:
            raise ValueError(
                f"Expected a non-empty value for `upload_collection_id` but received {upload_collection_id!r}"
            )
        return self._patch(
            path_template("/upload_collections/{upload_collection_id}", upload_collection_id=upload_collection_id),
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                upload_collection_update_params.UploadCollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCollection,
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
    ) -> UploadCollectionListResponse:
        """
        List upload collections.

        Args:
          id: The upload collection IDs to filter by.

          expand: Fields to expand on each upload collection in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The upload collection names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the upload collection results.

          slug: The upload collection slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/upload_collections",
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
                    upload_collection_list_params.UploadCollectionListParams,
                ),
            ),
            cast_to=UploadCollectionListResponse,
        )


class AsyncUploadCollectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncUploadCollectionsResourceWithStreamingResponse(self)

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
    ) -> UploadCollection:
        """
        Create a new upload collection.

        Args:
          name: The name of the upload collection.

          slug: An immutable, code-friendly name for the upload collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/upload_collections",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                upload_collection_create_params.UploadCollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCollection,
        )

    async def retrieve(
        self,
        upload_collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCollection:
        """
        Retrieve an upload collection by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_collection_id:
            raise ValueError(
                f"Expected a non-empty value for `upload_collection_id` but received {upload_collection_id!r}"
            )
        return await self._get(
            path_template("/upload_collections/{upload_collection_id}", upload_collection_id=upload_collection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCollection,
        )

    async def update(
        self,
        upload_collection_id: str,
        *,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCollection:
        """
        Update an upload collection by ID.

        Args:
          name: The updated name of the upload collection.

          slug: The updated slug for the upload collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_collection_id:
            raise ValueError(
                f"Expected a non-empty value for `upload_collection_id` but received {upload_collection_id!r}"
            )
        return await self._patch(
            path_template("/upload_collections/{upload_collection_id}", upload_collection_id=upload_collection_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                },
                upload_collection_update_params.UploadCollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCollection,
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
    ) -> UploadCollectionListResponse:
        """
        List upload collections.

        Args:
          id: The upload collection IDs to filter by.

          expand: Fields to expand on each upload collection in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The upload collection names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the upload collection results.

          slug: The upload collection slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/upload_collections",
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
                    upload_collection_list_params.UploadCollectionListParams,
                ),
            ),
            cast_to=UploadCollectionListResponse,
        )


class UploadCollectionsResourceWithRawResponse:
    def __init__(self, upload_collections: UploadCollectionsResource) -> None:
        self._upload_collections = upload_collections

        self.create = to_raw_response_wrapper(
            upload_collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            upload_collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            upload_collections.update,
        )
        self.list = to_raw_response_wrapper(
            upload_collections.list,
        )


class AsyncUploadCollectionsResourceWithRawResponse:
    def __init__(self, upload_collections: AsyncUploadCollectionsResource) -> None:
        self._upload_collections = upload_collections

        self.create = async_to_raw_response_wrapper(
            upload_collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            upload_collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            upload_collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            upload_collections.list,
        )


class UploadCollectionsResourceWithStreamingResponse:
    def __init__(self, upload_collections: UploadCollectionsResource) -> None:
        self._upload_collections = upload_collections

        self.create = to_streamed_response_wrapper(
            upload_collections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            upload_collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            upload_collections.update,
        )
        self.list = to_streamed_response_wrapper(
            upload_collections.list,
        )


class AsyncUploadCollectionsResourceWithStreamingResponse:
    def __init__(self, upload_collections: AsyncUploadCollectionsResource) -> None:
        self._upload_collections = upload_collections

        self.create = async_to_streamed_response_wrapper(
            upload_collections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            upload_collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            upload_collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            upload_collections.list,
        )
