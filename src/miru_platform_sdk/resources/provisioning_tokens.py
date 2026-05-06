# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.provisioning_token import ProvisioningToken

__all__ = ["ProvisioningTokensResource", "AsyncProvisioningTokensResource"]


class ProvisioningTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvisioningTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return ProvisioningTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvisioningTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return ProvisioningTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProvisioningToken:
        """Create a new provisioning token."""
        return self._post(
            "/provisioning_tokens",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProvisioningToken,
        )


class AsyncProvisioningTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvisioningTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProvisioningTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvisioningTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncProvisioningTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProvisioningToken:
        """Create a new provisioning token."""
        return await self._post(
            "/provisioning_tokens",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProvisioningToken,
        )


class ProvisioningTokensResourceWithRawResponse:
    def __init__(self, provisioning_tokens: ProvisioningTokensResource) -> None:
        self._provisioning_tokens = provisioning_tokens

        self.create = to_raw_response_wrapper(
            provisioning_tokens.create,
        )


class AsyncProvisioningTokensResourceWithRawResponse:
    def __init__(self, provisioning_tokens: AsyncProvisioningTokensResource) -> None:
        self._provisioning_tokens = provisioning_tokens

        self.create = async_to_raw_response_wrapper(
            provisioning_tokens.create,
        )


class ProvisioningTokensResourceWithStreamingResponse:
    def __init__(self, provisioning_tokens: ProvisioningTokensResource) -> None:
        self._provisioning_tokens = provisioning_tokens

        self.create = to_streamed_response_wrapper(
            provisioning_tokens.create,
        )


class AsyncProvisioningTokensResourceWithStreamingResponse:
    def __init__(self, provisioning_tokens: AsyncProvisioningTokensResource) -> None:
        self._provisioning_tokens = provisioning_tokens

        self.create = async_to_streamed_response_wrapper(
            provisioning_tokens.create,
        )
