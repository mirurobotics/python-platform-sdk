# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import (
    Device,
    DeviceList,
    DevicePingResponse,
    DeviceIssueActivationTokenResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        device = client.devices.create(
            name="Robot 1",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.devices.with_raw_response.create(
            name="Robot 1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.devices.with_streaming_response.create(
            name="Robot 1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        device = client.devices.retrieve(
            "dvc_123",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.devices.with_raw_response.retrieve(
            "dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.devices.with_streaming_response.retrieve(
            "dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Miru) -> None:
        device = client.devices.update(
            device_id="dvc_123",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Miru) -> None:
        device = client.devices.update(
            device_id="dvc_123",
            name="Robot 1",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Miru) -> None:
        response = client.devices.with_raw_response.update(
            device_id="dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Miru) -> None:
        with client.devices.with_streaming_response.update(
            device_id="dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.update(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        device = client.devices.list()
        assert_matches_type(DeviceList, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        device = client.devices.list(
            id=["dev_123"],
            agent_version=["v1.0.0"],
            expand=["total_count"],
            limit=1,
            name=["My Device"],
            offset=0,
            order_by=["id:asc"],
        )
        assert_matches_type(DeviceList, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceList, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceList, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_issue_activation_token(self, client: Miru) -> None:
        device = client.devices.issue_activation_token(
            device_id="dvc_123",
        )
        assert_matches_type(DeviceIssueActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_issue_activation_token_with_all_params(self, client: Miru) -> None:
        device = client.devices.issue_activation_token(
            device_id="dvc_123",
            allow_reactivation=False,
        )
        assert_matches_type(DeviceIssueActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_issue_activation_token(self, client: Miru) -> None:
        response = client.devices.with_raw_response.issue_activation_token(
            device_id="dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceIssueActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_issue_activation_token(self, client: Miru) -> None:
        with client.devices.with_streaming_response.issue_activation_token(
            device_id="dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceIssueActivationTokenResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_issue_activation_token(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.issue_activation_token(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ping(self, client: Miru) -> None:
        device = client.devices.ping(
            device_id="dvc_123",
            timeout_nanos=1000000000,
        )
        assert_matches_type(DevicePingResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ping(self, client: Miru) -> None:
        response = client.devices.with_raw_response.ping(
            device_id="dvc_123",
            timeout_nanos=1000000000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DevicePingResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ping(self, client: Miru) -> None:
        with client.devices.with_streaming_response.ping(
            device_id="dvc_123",
            timeout_nanos=1000000000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DevicePingResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_ping(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.ping(
                device_id="",
                timeout_nanos=1000000000,
            )


class TestAsyncDevices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.create(
            name="Robot 1",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.create(
            name="Robot 1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.create(
            name="Robot 1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.retrieve(
            "dvc_123",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.retrieve(
            "dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.retrieve(
            "dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.update(
            device_id="dvc_123",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.update(
            device_id="dvc_123",
            name="Robot 1",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.update(
            device_id="dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.update(
            device_id="dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.update(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.list()
        assert_matches_type(DeviceList, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.list(
            id=["dev_123"],
            agent_version=["v1.0.0"],
            expand=["total_count"],
            limit=1,
            name=["My Device"],
            offset=0,
            order_by=["id:asc"],
        )
        assert_matches_type(DeviceList, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceList, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceList, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_issue_activation_token(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.issue_activation_token(
            device_id="dvc_123",
        )
        assert_matches_type(DeviceIssueActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_issue_activation_token_with_all_params(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.issue_activation_token(
            device_id="dvc_123",
            allow_reactivation=False,
        )
        assert_matches_type(DeviceIssueActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_issue_activation_token(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.issue_activation_token(
            device_id="dvc_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceIssueActivationTokenResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_issue_activation_token(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.issue_activation_token(
            device_id="dvc_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceIssueActivationTokenResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_issue_activation_token(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.issue_activation_token(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ping(self, async_client: AsyncMiru) -> None:
        device = await async_client.devices.ping(
            device_id="dvc_123",
            timeout_nanos=1000000000,
        )
        assert_matches_type(DevicePingResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ping(self, async_client: AsyncMiru) -> None:
        response = await async_client.devices.with_raw_response.ping(
            device_id="dvc_123",
            timeout_nanos=1000000000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DevicePingResponse, device, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ping(self, async_client: AsyncMiru) -> None:
        async with async_client.devices.with_streaming_response.ping(
            device_id="dvc_123",
            timeout_nanos=1000000000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DevicePingResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_ping(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.ping(
                device_id="",
                timeout_nanos=1000000000,
            )
