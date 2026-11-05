# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import (
    Release,
    ReleaseList,
    DeletedRelease,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReleases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        release = client.releases.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Miru) -> None:
        release = client.releases.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            expand=["config_schemas"],
            description="Add lidar calibration to motion control",
            git_commit_ref={
                "id": "git_cmt_123",
                "sha": "1a2b3c4d...",
            },
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.releases.with_raw_response.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.releases.with_streaming_response.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        release = client.releases.retrieve(
            release_id="rls_123",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        release = client.releases.retrieve(
            release_id="rls_123",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.releases.with_raw_response.retrieve(
            release_id="rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.releases.with_streaming_response.retrieve(
            release_id="rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            client.releases.with_raw_response.retrieve(
                release_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        release = client.releases.list()
        assert_matches_type(ReleaseList, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        release = client.releases.list(
            id=["rls_123"],
            archived="false",
            expand=["config_schemas"],
            limit=10,
            offset=0,
            order_by=["created_at:desc"],
            version=["v1.0.0"],
        )
        assert_matches_type(ReleaseList, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.releases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(ReleaseList, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.releases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(ReleaseList, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Miru) -> None:
        release = client.releases.delete(
            "rls_123",
        )
        assert_matches_type(DeletedRelease, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Miru) -> None:
        response = client.releases.with_raw_response.delete(
            "rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(DeletedRelease, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Miru) -> None:
        with client.releases.with_streaming_response.delete(
            "rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(DeletedRelease, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            client.releases.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Miru) -> None:
        release = client.releases.archive(
            release_id="rls_123",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_with_all_params(self, client: Miru) -> None:
        release = client.releases.archive(
            release_id="rls_123",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Miru) -> None:
        response = client.releases.with_raw_response.archive(
            release_id="rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Miru) -> None:
        with client.releases.with_streaming_response.archive(
            release_id="rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            client.releases.with_raw_response.archive(
                release_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive(self, client: Miru) -> None:
        release = client.releases.unarchive(
            release_id="rls_123",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive_with_all_params(self, client: Miru) -> None:
        release = client.releases.unarchive(
            release_id="rls_123",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unarchive(self, client: Miru) -> None:
        response = client.releases.with_raw_response.unarchive(
            release_id="rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unarchive(self, client: Miru) -> None:
        with client.releases.with_streaming_response.unarchive(
            release_id="rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unarchive(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            client.releases.with_raw_response.unarchive(
                release_id="",
            )


class TestAsyncReleases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            expand=["config_schemas"],
            description="Add lidar calibration to motion control",
            git_commit_ref={
                "id": "git_cmt_123",
                "sha": "1a2b3c4d...",
            },
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.releases.with_raw_response.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.releases.with_streaming_response.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.retrieve(
            release_id="rls_123",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.retrieve(
            release_id="rls_123",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.releases.with_raw_response.retrieve(
            release_id="rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.releases.with_streaming_response.retrieve(
            release_id="rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            await async_client.releases.with_raw_response.retrieve(
                release_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.list()
        assert_matches_type(ReleaseList, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.list(
            id=["rls_123"],
            archived="false",
            expand=["config_schemas"],
            limit=10,
            offset=0,
            order_by=["created_at:desc"],
            version=["v1.0.0"],
        )
        assert_matches_type(ReleaseList, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.releases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(ReleaseList, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.releases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(ReleaseList, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.delete(
            "rls_123",
        )
        assert_matches_type(DeletedRelease, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMiru) -> None:
        response = await async_client.releases.with_raw_response.delete(
            "rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(DeletedRelease, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMiru) -> None:
        async with async_client.releases.with_streaming_response.delete(
            "rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(DeletedRelease, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            await async_client.releases.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.archive(
            release_id="rls_123",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.archive(
            release_id="rls_123",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMiru) -> None:
        response = await async_client.releases.with_raw_response.archive(
            release_id="rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMiru) -> None:
        async with async_client.releases.with_streaming_response.archive(
            release_id="rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            await async_client.releases.with_raw_response.archive(
                release_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.unarchive(
            release_id="rls_123",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive_with_all_params(self, async_client: AsyncMiru) -> None:
        release = await async_client.releases.unarchive(
            release_id="rls_123",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncMiru) -> None:
        response = await async_client.releases.with_raw_response.unarchive(
            release_id="rls_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncMiru) -> None:
        async with async_client.releases.with_streaming_response.unarchive(
            release_id="rls_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            await async_client.releases.with_raw_response.unarchive(
                release_id="",
            )
