# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform import MiruPlatform, AsyncMiruPlatform
from miru_platform.types import (
    Release,
    ReleaseListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReleases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: MiruPlatform) -> None:
        release = client.releases.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: MiruPlatform) -> None:
        release = client.releases.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            miru_version="2026-03-09.tetons",
            expand=["config_schemas"],
            git_commit_ref={
                "id": "git_cmt_123",
                "sha": "1a2b3c4d...",
            },
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: MiruPlatform) -> None:
        response = client.releases.with_raw_response.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: MiruPlatform) -> None:
        with client.releases.with_streaming_response.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: MiruPlatform) -> None:
        release = client.releases.retrieve(
            release_id="rls_123",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: MiruPlatform) -> None:
        release = client.releases.retrieve(
            release_id="rls_123",
            miru_version="2026-03-09.tetons",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: MiruPlatform) -> None:
        response = client.releases.with_raw_response.retrieve(
            release_id="rls_123",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: MiruPlatform) -> None:
        with client.releases.with_streaming_response.retrieve(
            release_id="rls_123",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: MiruPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            client.releases.with_raw_response.retrieve(
                release_id="",
                miru_version="2026-03-09.tetons",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: MiruPlatform) -> None:
        release = client.releases.list(
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: MiruPlatform) -> None:
        release = client.releases.list(
            miru_version="2026-03-09.tetons",
            id=["rls_123"],
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by=["id:asc"],
            version=["v1.0.0"],
        )
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: MiruPlatform) -> None:
        response = client.releases.with_raw_response.list(
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = response.parse()
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: MiruPlatform) -> None:
        with client.releases.with_streaming_response.list(
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = response.parse()
            assert_matches_type(ReleaseListResponse, release, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReleases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiruPlatform) -> None:
        release = await async_client.releases.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMiruPlatform) -> None:
        release = await async_client.releases.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            miru_version="2026-03-09.tetons",
            expand=["config_schemas"],
            git_commit_ref={
                "id": "git_cmt_123",
                "sha": "1a2b3c4d...",
            },
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.releases.with_raw_response.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.releases.with_streaming_response.create(
            config_schema_ids=["cfg_sch_123"],
            version="v1.0.0",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        release = await async_client.releases.retrieve(
            release_id="rls_123",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiruPlatform) -> None:
        release = await async_client.releases.retrieve(
            release_id="rls_123",
            miru_version="2026-03-09.tetons",
            expand=["config_schemas"],
        )
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.releases.with_raw_response.retrieve(
            release_id="rls_123",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(Release, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.releases.with_streaming_response.retrieve(
            release_id="rls_123",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(Release, release, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `release_id` but received ''"):
            await async_client.releases.with_raw_response.retrieve(
                release_id="",
                miru_version="2026-03-09.tetons",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiruPlatform) -> None:
        release = await async_client.releases.list(
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiruPlatform) -> None:
        release = await async_client.releases.list(
            miru_version="2026-03-09.tetons",
            id=["rls_123"],
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by=["id:asc"],
            version=["v1.0.0"],
        )
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.releases.with_raw_response.list(
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release = await response.parse()
        assert_matches_type(ReleaseListResponse, release, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.releases.with_streaming_response.list(
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release = await response.parse()
            assert_matches_type(ReleaseListResponse, release, path=["response"])

        assert cast(Any, response.is_closed) is True
