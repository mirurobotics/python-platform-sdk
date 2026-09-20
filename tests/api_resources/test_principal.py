# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import Principal

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrincipal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_self(self, client: Miru) -> None:
        principal = client.principal.self()
        assert_matches_type(Principal, principal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_self(self, client: Miru) -> None:
        response = client.principal.with_raw_response.self()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principal = response.parse()
        assert_matches_type(Principal, principal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_self(self, client: Miru) -> None:
        with client.principal.with_streaming_response.self() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principal = response.parse()
            assert_matches_type(Principal, principal, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrincipal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_self(self, async_client: AsyncMiru) -> None:
        principal = await async_client.principal.self()
        assert_matches_type(Principal, principal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_self(self, async_client: AsyncMiru) -> None:
        response = await async_client.principal.with_raw_response.self()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principal = await response.parse()
        assert_matches_type(Principal, principal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_self(self, async_client: AsyncMiru) -> None:
        async with async_client.principal.with_streaming_response.self() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principal = await response.parse()
            assert_matches_type(Principal, principal, path=["response"])

        assert cast(Any, response.is_closed) is True
