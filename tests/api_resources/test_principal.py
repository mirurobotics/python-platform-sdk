# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform import MiruPlatform, AsyncMiruPlatform
from miru_platform.types import PrincipalIdentifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrincipal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_identify(self, client: MiruPlatform) -> None:
        principal = client.principal.identify(
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(PrincipalIdentifyResponse, principal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_identify(self, client: MiruPlatform) -> None:
        response = client.principal.with_raw_response.identify(
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principal = response.parse()
        assert_matches_type(PrincipalIdentifyResponse, principal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_identify(self, client: MiruPlatform) -> None:
        with client.principal.with_streaming_response.identify(
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principal = response.parse()
            assert_matches_type(PrincipalIdentifyResponse, principal, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrincipal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_identify(self, async_client: AsyncMiruPlatform) -> None:
        principal = await async_client.principal.identify(
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(PrincipalIdentifyResponse, principal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_identify(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.principal.with_raw_response.identify(
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principal = await response.parse()
        assert_matches_type(PrincipalIdentifyResponse, principal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_identify(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.principal.with_streaming_response.identify(
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principal = await response.parse()
            assert_matches_type(PrincipalIdentifyResponse, principal, path=["response"])

        assert cast(Any, response.is_closed) is True
