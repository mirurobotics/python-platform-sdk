# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import (
    ConfigType,
    ConfigTypeListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        config_type = client.config_types.create(
            name="My Config Type",
            slug="my-config-type",
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Miru) -> None:
        config_type = client.config_types.create(
            name="My Config Type",
            slug="my-config-type",
            expand=["config_schemas"],
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.config_types.with_raw_response.create(
            name="My Config Type",
            slug="my-config-type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_type = response.parse()
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.config_types.with_streaming_response.create(
            name="My Config Type",
            slug="my-config-type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_type = response.parse()
            assert_matches_type(ConfigType, config_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        config_type = client.config_types.retrieve(
            config_type_id="cfg_typ_123",
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        config_type = client.config_types.retrieve(
            config_type_id="cfg_typ_123",
            expand=["config_schemas"],
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.config_types.with_raw_response.retrieve(
            config_type_id="cfg_typ_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_type = response.parse()
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.config_types.with_streaming_response.retrieve(
            config_type_id="cfg_typ_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_type = response.parse()
            assert_matches_type(ConfigType, config_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_type_id` but received ''"):
            client.config_types.with_raw_response.retrieve(
                config_type_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Miru) -> None:
        config_type = client.config_types.update(
            config_type_id="cfg_typ_123",
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Miru) -> None:
        config_type = client.config_types.update(
            config_type_id="cfg_typ_123",
            expand=["config_schemas"],
            name="My Config Type",
            slug="my-config-type",
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Miru) -> None:
        response = client.config_types.with_raw_response.update(
            config_type_id="cfg_typ_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_type = response.parse()
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Miru) -> None:
        with client.config_types.with_streaming_response.update(
            config_type_id="cfg_typ_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_type = response.parse()
            assert_matches_type(ConfigType, config_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_type_id` but received ''"):
            client.config_types.with_raw_response.update(
                config_type_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        config_type = client.config_types.list()
        assert_matches_type(ConfigTypeListResponse, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        config_type = client.config_types.list(
            id=["cfg_typ_123"],
            expand=["total_count"],
            limit=1,
            name=["Motion Control"],
            offset=0,
            order_by=["id:asc"],
            slug=["motion-control"],
        )
        assert_matches_type(ConfigTypeListResponse, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.config_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_type = response.parse()
        assert_matches_type(ConfigTypeListResponse, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.config_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_type = response.parse()
            assert_matches_type(ConfigTypeListResponse, config_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        config_type = await async_client.config_types.create(
            name="My Config Type",
            slug="my-config-type",
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMiru) -> None:
        config_type = await async_client.config_types.create(
            name="My Config Type",
            slug="my-config-type",
            expand=["config_schemas"],
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_types.with_raw_response.create(
            name="My Config Type",
            slug="my-config-type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_type = await response.parse()
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.config_types.with_streaming_response.create(
            name="My Config Type",
            slug="my-config-type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_type = await response.parse()
            assert_matches_type(ConfigType, config_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        config_type = await async_client.config_types.retrieve(
            config_type_id="cfg_typ_123",
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        config_type = await async_client.config_types.retrieve(
            config_type_id="cfg_typ_123",
            expand=["config_schemas"],
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_types.with_raw_response.retrieve(
            config_type_id="cfg_typ_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_type = await response.parse()
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.config_types.with_streaming_response.retrieve(
            config_type_id="cfg_typ_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_type = await response.parse()
            assert_matches_type(ConfigType, config_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_type_id` but received ''"):
            await async_client.config_types.with_raw_response.retrieve(
                config_type_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMiru) -> None:
        config_type = await async_client.config_types.update(
            config_type_id="cfg_typ_123",
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMiru) -> None:
        config_type = await async_client.config_types.update(
            config_type_id="cfg_typ_123",
            expand=["config_schemas"],
            name="My Config Type",
            slug="my-config-type",
        )
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_types.with_raw_response.update(
            config_type_id="cfg_typ_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_type = await response.parse()
        assert_matches_type(ConfigType, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMiru) -> None:
        async with async_client.config_types.with_streaming_response.update(
            config_type_id="cfg_typ_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_type = await response.parse()
            assert_matches_type(ConfigType, config_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_type_id` but received ''"):
            await async_client.config_types.with_raw_response.update(
                config_type_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        config_type = await async_client.config_types.list()
        assert_matches_type(ConfigTypeListResponse, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        config_type = await async_client.config_types.list(
            id=["cfg_typ_123"],
            expand=["total_count"],
            limit=1,
            name=["Motion Control"],
            offset=0,
            order_by=["id:asc"],
            slug=["motion-control"],
        )
        assert_matches_type(ConfigTypeListResponse, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_type = await response.parse()
        assert_matches_type(ConfigTypeListResponse, config_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.config_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_type = await response.parse()
            assert_matches_type(ConfigTypeListResponse, config_type, path=["response"])

        assert cast(Any, response.is_closed) is True
