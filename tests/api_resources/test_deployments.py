# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import (
    Deployment,
    DeploymentList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        deployment = client.deployments.create(
            config_instance_ids=["cfg_inst_123"],
            description="Deployment for the motion control config instance",
            device_id="dvc_123",
            release_id="rls_123",
            target_status="staged",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Miru) -> None:
        deployment = client.deployments.create(
            config_instance_ids=["cfg_inst_123"],
            description="Deployment for the motion control config instance",
            device_id="dvc_123",
            release_id="rls_123",
            target_status="staged",
            expand=["device"],
            parent_id="dpl_123",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.deployments.with_raw_response.create(
            config_instance_ids=["cfg_inst_123"],
            description="Deployment for the motion control config instance",
            device_id="dvc_123",
            release_id="rls_123",
            target_status="staged",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.deployments.with_streaming_response.create(
            config_instance_ids=["cfg_inst_123"],
            description="Deployment for the motion control config instance",
            device_id="dvc_123",
            release_id="rls_123",
            target_status="staged",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        deployment = client.deployments.retrieve(
            deployment_id="dpl_123",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        deployment = client.deployments.retrieve(
            deployment_id="dpl_123",
            expand=["device"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.deployments.with_raw_response.retrieve(
            deployment_id="dpl_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.deployments.with_streaming_response.retrieve(
            deployment_id="dpl_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.deployments.with_raw_response.retrieve(
                deployment_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        deployment = client.deployments.list()
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        deployment = client.deployments.list(
            id=["dpl_123"],
            activity_status=["drifted"],
            device_id=["dvc_123"],
            error_status=["none"],
            expand=["device"],
            limit=10,
            offset=0,
            order_by=["created_at:desc"],
            release_id=["rls_123"],
            target_status=["staged"],
        )
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.deployments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.deployments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Miru) -> None:
        deployment = client.deployments.archive(
            deployment_id="dpl_123",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_with_all_params(self, client: Miru) -> None:
        deployment = client.deployments.archive(
            deployment_id="dpl_123",
            expand=["device"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Miru) -> None:
        response = client.deployments.with_raw_response.archive(
            deployment_id="dpl_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Miru) -> None:
        with client.deployments.with_streaming_response.archive(
            deployment_id="dpl_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.deployments.with_raw_response.archive(
                deployment_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deploy(self, client: Miru) -> None:
        deployment = client.deployments.deploy(
            deployment_id="dpl_123",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deploy_with_all_params(self, client: Miru) -> None:
        deployment = client.deployments.deploy(
            deployment_id="dpl_123",
            expand=["device"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deploy(self, client: Miru) -> None:
        response = client.deployments.with_raw_response.deploy(
            deployment_id="dpl_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deploy(self, client: Miru) -> None:
        with client.deployments.with_streaming_response.deploy(
            deployment_id="dpl_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deploy(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.deployments.with_raw_response.deploy(
                deployment_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_drifts(self, client: Miru) -> None:
        deployment = client.deployments.list_drifts(
            deployment_id="dpl_123",
        )
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_drifts_with_all_params(self, client: Miru) -> None:
        deployment = client.deployments.list_drifts(
            deployment_id="dpl_123",
            expand=["device"],
        )
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_drifts(self, client: Miru) -> None:
        response = client.deployments.with_raw_response.list_drifts(
            deployment_id="dpl_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_drifts(self, client: Miru) -> None:
        with client.deployments.with_streaming_response.list_drifts(
            deployment_id="dpl_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_drifts(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.deployments.with_raw_response.list_drifts(
                deployment_id="",
            )


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.create(
            config_instance_ids=["cfg_inst_123"],
            description="Deployment for the motion control config instance",
            device_id="dvc_123",
            release_id="rls_123",
            target_status="staged",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.create(
            config_instance_ids=["cfg_inst_123"],
            description="Deployment for the motion control config instance",
            device_id="dvc_123",
            release_id="rls_123",
            target_status="staged",
            expand=["device"],
            parent_id="dpl_123",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.deployments.with_raw_response.create(
            config_instance_ids=["cfg_inst_123"],
            description="Deployment for the motion control config instance",
            device_id="dvc_123",
            release_id="rls_123",
            target_status="staged",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.deployments.with_streaming_response.create(
            config_instance_ids=["cfg_inst_123"],
            description="Deployment for the motion control config instance",
            device_id="dvc_123",
            release_id="rls_123",
            target_status="staged",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.retrieve(
            deployment_id="dpl_123",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.retrieve(
            deployment_id="dpl_123",
            expand=["device"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.deployments.with_raw_response.retrieve(
            deployment_id="dpl_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.deployments.with_streaming_response.retrieve(
            deployment_id="dpl_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.deployments.with_raw_response.retrieve(
                deployment_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.list()
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.list(
            id=["dpl_123"],
            activity_status=["drifted"],
            device_id=["dvc_123"],
            error_status=["none"],
            expand=["device"],
            limit=10,
            offset=0,
            order_by=["created_at:desc"],
            release_id=["rls_123"],
            target_status=["staged"],
        )
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.deployments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.deployments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.archive(
            deployment_id="dpl_123",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.archive(
            deployment_id="dpl_123",
            expand=["device"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMiru) -> None:
        response = await async_client.deployments.with_raw_response.archive(
            deployment_id="dpl_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMiru) -> None:
        async with async_client.deployments.with_streaming_response.archive(
            deployment_id="dpl_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.deployments.with_raw_response.archive(
                deployment_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deploy(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.deploy(
            deployment_id="dpl_123",
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deploy_with_all_params(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.deploy(
            deployment_id="dpl_123",
            expand=["device"],
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deploy(self, async_client: AsyncMiru) -> None:
        response = await async_client.deployments.with_raw_response.deploy(
            deployment_id="dpl_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deploy(self, async_client: AsyncMiru) -> None:
        async with async_client.deployments.with_streaming_response.deploy(
            deployment_id="dpl_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deploy(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.deployments.with_raw_response.deploy(
                deployment_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_drifts(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.list_drifts(
            deployment_id="dpl_123",
        )
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_drifts_with_all_params(self, async_client: AsyncMiru) -> None:
        deployment = await async_client.deployments.list_drifts(
            deployment_id="dpl_123",
            expand=["device"],
        )
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_drifts(self, async_client: AsyncMiru) -> None:
        response = await async_client.deployments.with_raw_response.list_drifts(
            deployment_id="dpl_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentList, deployment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_drifts(self, async_client: AsyncMiru) -> None:
        async with async_client.deployments.with_streaming_response.list_drifts(
            deployment_id="dpl_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_drifts(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.deployments.with_raw_response.list_drifts(
                deployment_id="",
            )
