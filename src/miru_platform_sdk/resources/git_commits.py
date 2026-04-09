# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import git_commit_list_params, git_commit_create_params
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
from ..types.git_commit import GitCommit
from ..types.git_commit_list import GitCommitList

__all__ = ["GitCommitsResource", "AsyncGitCommitsResource"]


class GitCommitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GitCommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return GitCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return GitCommitsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        message: str,
        origin: str,
        sha: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitCommit:
        """
        Register a git commit.

        Args:
          message: The commit message.

          origin: The URL of the git repository origin.

          sha: The SHA hash of the git commit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/git_commits",
            body=maybe_transform(
                {
                    "message": message,
                    "origin": origin,
                    "sha": sha,
                },
                git_commit_create_params.GitCommitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitCommit,
        )

    def retrieve(
        self,
        git_commit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitCommit:
        """
        Retrieve a git commit by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not git_commit_id:
            raise ValueError(f"Expected a non-empty value for `git_commit_id` but received {git_commit_id!r}")
        return self._get(
            path_template("/git_commits/{git_commit_id}", git_commit_id=git_commit_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitCommit,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        sha: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitCommitList:
        """
        List git commits.

        Args:
          id: The git commit IDs to filter by.

          expand: Fields to expand on each git commit in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the git commit results.

          sha: The git commit SHAs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/git_commits",
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
                        "offset": offset,
                        "order_by": order_by,
                        "sha": sha,
                    },
                    git_commit_list_params.GitCommitListParams,
                ),
            ),
            cast_to=GitCommitList,
        )


class AsyncGitCommitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGitCommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGitCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncGitCommitsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        message: str,
        origin: str,
        sha: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitCommit:
        """
        Register a git commit.

        Args:
          message: The commit message.

          origin: The URL of the git repository origin.

          sha: The SHA hash of the git commit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/git_commits",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "origin": origin,
                    "sha": sha,
                },
                git_commit_create_params.GitCommitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitCommit,
        )

    async def retrieve(
        self,
        git_commit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitCommit:
        """
        Retrieve a git commit by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not git_commit_id:
            raise ValueError(f"Expected a non-empty value for `git_commit_id` but received {git_commit_id!r}")
        return await self._get(
            path_template("/git_commits/{git_commit_id}", git_commit_id=git_commit_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitCommit,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        sha: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitCommitList:
        """
        List git commits.

        Args:
          id: The git commit IDs to filter by.

          expand: Fields to expand on each git commit in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the git commit results.

          sha: The git commit SHAs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/git_commits",
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
                        "offset": offset,
                        "order_by": order_by,
                        "sha": sha,
                    },
                    git_commit_list_params.GitCommitListParams,
                ),
            ),
            cast_to=GitCommitList,
        )


class GitCommitsResourceWithRawResponse:
    def __init__(self, git_commits: GitCommitsResource) -> None:
        self._git_commits = git_commits

        self.create = to_raw_response_wrapper(
            git_commits.create,
        )
        self.retrieve = to_raw_response_wrapper(
            git_commits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            git_commits.list,
        )


class AsyncGitCommitsResourceWithRawResponse:
    def __init__(self, git_commits: AsyncGitCommitsResource) -> None:
        self._git_commits = git_commits

        self.create = async_to_raw_response_wrapper(
            git_commits.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            git_commits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            git_commits.list,
        )


class GitCommitsResourceWithStreamingResponse:
    def __init__(self, git_commits: GitCommitsResource) -> None:
        self._git_commits = git_commits

        self.create = to_streamed_response_wrapper(
            git_commits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            git_commits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            git_commits.list,
        )


class AsyncGitCommitsResourceWithStreamingResponse:
    def __init__(self, git_commits: AsyncGitCommitsResource) -> None:
        self._git_commits = git_commits

        self.create = async_to_streamed_response_wrapper(
            git_commits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            git_commits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            git_commits.list,
        )
