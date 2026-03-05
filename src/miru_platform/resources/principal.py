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
from ..types.principal_identify_response import PrincipalIdentifyResponse

__all__ = ["PrincipalResource", "AsyncPrincipalResource"]


class PrincipalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrincipalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-platform-python#accessing-raw-response-data-eg-headers
        """
        return PrincipalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrincipalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-platform-python#with_streaming_response
        """
        return PrincipalResourceWithStreamingResponse(self)

    def identify(
        self,
        *,
        miru_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrincipalIdentifyResponse:
        """Identify the currently authenticated principal.

        Returns the identity associated
        with the API key used in the request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Miru-Version": miru_version, **(extra_headers or {})}
        return self._get(
            "/principal",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrincipalIdentifyResponse,
        )


class AsyncPrincipalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrincipalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrincipalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrincipalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-platform-python#with_streaming_response
        """
        return AsyncPrincipalResourceWithStreamingResponse(self)

    async def identify(
        self,
        *,
        miru_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrincipalIdentifyResponse:
        """Identify the currently authenticated principal.

        Returns the identity associated
        with the API key used in the request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Miru-Version": miru_version, **(extra_headers or {})}
        return await self._get(
            "/principal",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrincipalIdentifyResponse,
        )


class PrincipalResourceWithRawResponse:
    def __init__(self, principal: PrincipalResource) -> None:
        self._principal = principal

        self.identify = to_raw_response_wrapper(
            principal.identify,
        )


class AsyncPrincipalResourceWithRawResponse:
    def __init__(self, principal: AsyncPrincipalResource) -> None:
        self._principal = principal

        self.identify = async_to_raw_response_wrapper(
            principal.identify,
        )


class PrincipalResourceWithStreamingResponse:
    def __init__(self, principal: PrincipalResource) -> None:
        self._principal = principal

        self.identify = to_streamed_response_wrapper(
            principal.identify,
        )


class AsyncPrincipalResourceWithStreamingResponse:
    def __init__(self, principal: AsyncPrincipalResource) -> None:
        self._principal = principal

        self.identify = async_to_streamed_response_wrapper(
            principal.identify,
        )
