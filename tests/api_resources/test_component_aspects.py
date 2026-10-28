# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import (
    ComponentAspect,
    ComponentAspectList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComponentAspects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        component_aspect = client.component_aspects.retrieve(
            component_aspect_id="cmp_asp_123",
        )
        assert_matches_type(ComponentAspect, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        component_aspect = client.component_aspects.retrieve(
            component_aspect_id="cmp_asp_123",
            expand=["component"],
        )
        assert_matches_type(ComponentAspect, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.component_aspects.with_raw_response.retrieve(
            component_aspect_id="cmp_asp_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        component_aspect = response.parse()
        assert_matches_type(ComponentAspect, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.component_aspects.with_streaming_response.retrieve(
            component_aspect_id="cmp_asp_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            component_aspect = response.parse()
            assert_matches_type(ComponentAspect, component_aspect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `component_aspect_id` but received ''"):
            client.component_aspects.with_raw_response.retrieve(
                component_aspect_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        component_aspect = client.component_aspects.list()
        assert_matches_type(ComponentAspectList, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        component_aspect = client.component_aspects.list(
            id=["cmp_asp_123"],
            component_id=["cmp_123"],
            expand=["component"],
            limit=10,
            name=["Joint Offsets"],
            offset=0,
            order_by=["created_at:asc"],
            slug=["joint-offsets"],
        )
        assert_matches_type(ComponentAspectList, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.component_aspects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        component_aspect = response.parse()
        assert_matches_type(ComponentAspectList, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.component_aspects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            component_aspect = response.parse()
            assert_matches_type(ComponentAspectList, component_aspect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncComponentAspects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        component_aspect = await async_client.component_aspects.retrieve(
            component_aspect_id="cmp_asp_123",
        )
        assert_matches_type(ComponentAspect, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        component_aspect = await async_client.component_aspects.retrieve(
            component_aspect_id="cmp_asp_123",
            expand=["component"],
        )
        assert_matches_type(ComponentAspect, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.component_aspects.with_raw_response.retrieve(
            component_aspect_id="cmp_asp_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        component_aspect = await response.parse()
        assert_matches_type(ComponentAspect, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.component_aspects.with_streaming_response.retrieve(
            component_aspect_id="cmp_asp_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            component_aspect = await response.parse()
            assert_matches_type(ComponentAspect, component_aspect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `component_aspect_id` but received ''"):
            await async_client.component_aspects.with_raw_response.retrieve(
                component_aspect_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        component_aspect = await async_client.component_aspects.list()
        assert_matches_type(ComponentAspectList, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        component_aspect = await async_client.component_aspects.list(
            id=["cmp_asp_123"],
            component_id=["cmp_123"],
            expand=["component"],
            limit=10,
            name=["Joint Offsets"],
            offset=0,
            order_by=["created_at:asc"],
            slug=["joint-offsets"],
        )
        assert_matches_type(ComponentAspectList, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.component_aspects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        component_aspect = await response.parse()
        assert_matches_type(ComponentAspectList, component_aspect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.component_aspects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            component_aspect = await response.parse()
            assert_matches_type(ComponentAspectList, component_aspect, path=["response"])

        assert cast(Any, response.is_closed) is True
