# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    group_list_params,
    group_move_params,
    group_create_params,
    group_update_params,
    group_retrieve_params,
)
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
from ..types.group import Group
from .._base_client import make_request_options
from ..types.group_list import GroupList

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        expand: List[Literal["parent"]] | Omit = omit,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Create a new group.

        Args:
          name: The name of the group.

          expand: Fields to expand on the group resource.

          parent_id: ID of the parent group. Omit or set to null to create a top-level group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/groups",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, group_create_params.GroupCreateParams),
            ),
            cast_to=Group,
        )

    def retrieve(
        self,
        group_id: str,
        *,
        expand: List[Literal["parent"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Retrieve a group by ID.

        Args:
          expand: Fields to expand on the group resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            path_template("/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, group_retrieve_params.GroupRetrieveParams),
            ),
            cast_to=Group,
        )

    def update(
        self,
        group_id: str,
        *,
        expand: List[Literal["parent"]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Update a group.

        Args:
          expand: Fields to expand on the group resource.

          name: The updated name of the group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._patch(
            path_template("/groups/{group_id}", group_id=group_id),
            body=maybe_transform({"name": name}, group_update_params.GroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, group_update_params.GroupUpdateParams),
            ),
            cast_to=Group,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "parent"]] | Omit = omit,
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
        parent_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupList:
        """
        List groups.

        Args:
          id: The group IDs to filter by.

          expand: Fields to expand on each group in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The group names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the group results.

          parent_id: The parent group IDs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/groups",
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
                        "parent_id": parent_id,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            cast_to=GroupList,
        )

    def move(
        self,
        group_id: str,
        *,
        parent_id: Optional[str],
        expand: List[Literal["parent"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Move a group to a new parent, or to the top level by setting parent_id to null.

        Args:
          parent_id: ID of the new parent group. Set to null to make this a top-level group.

          expand: Fields to expand on the group resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            path_template("/groups/{group_id}/move", group_id=group_id),
            body=maybe_transform({"parent_id": parent_id}, group_move_params.GroupMoveParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, group_move_params.GroupMoveParams),
            ),
            cast_to=Group,
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        expand: List[Literal["parent"]] | Omit = omit,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Create a new group.

        Args:
          name: The name of the group.

          expand: Fields to expand on the group resource.

          parent_id: ID of the parent group. Omit or set to null to create a top-level group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, group_create_params.GroupCreateParams),
            ),
            cast_to=Group,
        )

    async def retrieve(
        self,
        group_id: str,
        *,
        expand: List[Literal["parent"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Retrieve a group by ID.

        Args:
          expand: Fields to expand on the group resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            path_template("/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, group_retrieve_params.GroupRetrieveParams),
            ),
            cast_to=Group,
        )

    async def update(
        self,
        group_id: str,
        *,
        expand: List[Literal["parent"]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Update a group.

        Args:
          expand: Fields to expand on the group resource.

          name: The updated name of the group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._patch(
            path_template("/groups/{group_id}", group_id=group_id),
            body=await async_maybe_transform({"name": name}, group_update_params.GroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, group_update_params.GroupUpdateParams),
            ),
            cast_to=Group,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count", "parent"]] | Omit = omit,
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
        parent_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupList:
        """
        List groups.

        Args:
          id: The group IDs to filter by.

          expand: Fields to expand on each group in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          name: The group names to filter by.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the group results.

          parent_id: The parent group IDs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/groups",
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
                        "parent_id": parent_id,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            cast_to=GroupList,
        )

    async def move(
        self,
        group_id: str,
        *,
        parent_id: Optional[str],
        expand: List[Literal["parent"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Move a group to a new parent, or to the top level by setting parent_id to null.

        Args:
          parent_id: ID of the new parent group. Set to null to make this a top-level group.

          expand: Fields to expand on the group resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            path_template("/groups/{group_id}/move", group_id=group_id),
            body=await async_maybe_transform({"parent_id": parent_id}, group_move_params.GroupMoveParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, group_move_params.GroupMoveParams),
            ),
            cast_to=Group,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.list = to_raw_response_wrapper(
            groups.list,
        )
        self.move = to_raw_response_wrapper(
            groups.move,
        )


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            groups.list,
        )
        self.move = async_to_raw_response_wrapper(
            groups.move,
        )


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.list = to_streamed_response_wrapper(
            groups.list,
        )
        self.move = to_streamed_response_wrapper(
            groups.move,
        )


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
        self.move = async_to_streamed_response_wrapper(
            groups.move,
        )
