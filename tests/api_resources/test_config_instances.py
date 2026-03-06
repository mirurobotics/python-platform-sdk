# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import (
    ConfigInstance,
    ConfigInstanceListResponse,
)
from miru_platform_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        config_instance = client.config_instances.create(
            config_schema_id="cfg_sch_123",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Miru) -> None:
        config_instance = client.config_instances.create(
            config_schema_id="cfg_sch_123",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
            expand=["content"],
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.config_instances.with_raw_response.create(
            config_schema_id="cfg_sch_123",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = response.parse()
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.config_instances.with_streaming_response.create(
            config_schema_id="cfg_sch_123",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = response.parse()
            assert_matches_type(ConfigInstance, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        config_instance = client.config_instances.retrieve(
            config_instance_id="cfg_inst_123",
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        config_instance = client.config_instances.retrieve(
            config_instance_id="cfg_inst_123",
            expand=["content"],
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.config_instances.with_raw_response.retrieve(
            config_instance_id="cfg_inst_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = response.parse()
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.config_instances.with_streaming_response.retrieve(
            config_instance_id="cfg_inst_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = response.parse()
            assert_matches_type(ConfigInstance, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_instance_id` but received ''"):
            client.config_instances.with_raw_response.retrieve(
                config_instance_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        config_instance = client.config_instances.list()
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        config_instance = client.config_instances.list(
            id=["cfg_inst_123"],
            config_schema_id=["cfg_sch_123"],
            config_type_id=["cfg_typ_123"],
            expand=["content"],
            limit=10,
            offset=0,
            order_by=["created_at:desc"],
        )
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.config_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = response.parse()
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.config_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = response.parse()
            assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_content(self, client: Miru, respx_mock: MockRouter) -> None:
        respx_mock.get("/config_instances/cfg_inst_123/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        config_instance = client.config_instances.content(
            config_instance_id="cfg_inst_123",
        )
        assert config_instance.is_closed
        assert config_instance.json() == {"foo": "bar"}
        assert cast(Any, config_instance.is_closed) is True
        assert isinstance(config_instance, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_content_with_all_params(self, client: Miru, respx_mock: MockRouter) -> None:
        respx_mock.get("/config_instances/cfg_inst_123/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        config_instance = client.config_instances.content(
            config_instance_id="cfg_inst_123",
            disposition="inline",
        )
        assert config_instance.is_closed
        assert config_instance.json() == {"foo": "bar"}
        assert cast(Any, config_instance.is_closed) is True
        assert isinstance(config_instance, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_content(self, client: Miru, respx_mock: MockRouter) -> None:
        respx_mock.get("/config_instances/cfg_inst_123/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        config_instance = client.config_instances.with_raw_response.content(
            config_instance_id="cfg_inst_123",
        )

        assert config_instance.is_closed is True
        assert config_instance.http_request.headers.get("X-Stainless-Lang") == "python"
        assert config_instance.json() == {"foo": "bar"}
        assert isinstance(config_instance, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_content(self, client: Miru, respx_mock: MockRouter) -> None:
        respx_mock.get("/config_instances/cfg_inst_123/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.config_instances.with_streaming_response.content(
            config_instance_id="cfg_inst_123",
        ) as config_instance:
            assert not config_instance.is_closed
            assert config_instance.http_request.headers.get("X-Stainless-Lang") == "python"

            assert config_instance.json() == {"foo": "bar"}
            assert cast(Any, config_instance.is_closed) is True
            assert isinstance(config_instance, StreamedBinaryAPIResponse)

        assert cast(Any, config_instance.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_content(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_instance_id` but received ''"):
            client.config_instances.with_raw_response.content(
                config_instance_id="",
            )


class TestAsyncConfigInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.create(
            config_schema_id="cfg_sch_123",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.create(
            config_schema_id="cfg_sch_123",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
            expand=["content"],
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_instances.with_raw_response.create(
            config_schema_id="cfg_sch_123",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = await response.parse()
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.config_instances.with_streaming_response.create(
            config_schema_id="cfg_sch_123",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = await response.parse()
            assert_matches_type(ConfigInstance, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.retrieve(
            config_instance_id="cfg_inst_123",
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.retrieve(
            config_instance_id="cfg_inst_123",
            expand=["content"],
        )
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_instances.with_raw_response.retrieve(
            config_instance_id="cfg_inst_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = await response.parse()
        assert_matches_type(ConfigInstance, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.config_instances.with_streaming_response.retrieve(
            config_instance_id="cfg_inst_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = await response.parse()
            assert_matches_type(ConfigInstance, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_instance_id` but received ''"):
            await async_client.config_instances.with_raw_response.retrieve(
                config_instance_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.list()
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        config_instance = await async_client.config_instances.list(
            id=["cfg_inst_123"],
            config_schema_id=["cfg_sch_123"],
            config_type_id=["cfg_typ_123"],
            expand=["content"],
            limit=10,
            offset=0,
            order_by=["created_at:desc"],
        )
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.config_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = await response.parse()
        assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.config_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = await response.parse()
            assert_matches_type(ConfigInstanceListResponse, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_content(self, async_client: AsyncMiru, respx_mock: MockRouter) -> None:
        respx_mock.get("/config_instances/cfg_inst_123/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        config_instance = await async_client.config_instances.content(
            config_instance_id="cfg_inst_123",
        )
        assert config_instance.is_closed
        assert await config_instance.json() == {"foo": "bar"}
        assert cast(Any, config_instance.is_closed) is True
        assert isinstance(config_instance, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_content_with_all_params(self, async_client: AsyncMiru, respx_mock: MockRouter) -> None:
        respx_mock.get("/config_instances/cfg_inst_123/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        config_instance = await async_client.config_instances.content(
            config_instance_id="cfg_inst_123",
            disposition="inline",
        )
        assert config_instance.is_closed
        assert await config_instance.json() == {"foo": "bar"}
        assert cast(Any, config_instance.is_closed) is True
        assert isinstance(config_instance, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_content(self, async_client: AsyncMiru, respx_mock: MockRouter) -> None:
        respx_mock.get("/config_instances/cfg_inst_123/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        config_instance = await async_client.config_instances.with_raw_response.content(
            config_instance_id="cfg_inst_123",
        )

        assert config_instance.is_closed is True
        assert config_instance.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await config_instance.json() == {"foo": "bar"}
        assert isinstance(config_instance, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_content(self, async_client: AsyncMiru, respx_mock: MockRouter) -> None:
        respx_mock.get("/config_instances/cfg_inst_123/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.config_instances.with_streaming_response.content(
            config_instance_id="cfg_inst_123",
        ) as config_instance:
            assert not config_instance.is_closed
            assert config_instance.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await config_instance.json() == {"foo": "bar"}
            assert cast(Any, config_instance.is_closed) is True
            assert isinstance(config_instance, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, config_instance.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_content(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_instance_id` but received ''"):
            await async_client.config_instances.with_raw_response.content(
                config_instance_id="",
            )
