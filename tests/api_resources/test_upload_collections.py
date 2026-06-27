# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import (
    UploadCollection,
    UploadCollectionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploadCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        upload_collection = client.upload_collections.create(
            name="Robot Logs",
            slug="robot-logs",
        )
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.upload_collections.with_raw_response.create(
            name="Robot Logs",
            slug="robot-logs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_collection = response.parse()
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.upload_collections.with_streaming_response.create(
            name="Robot Logs",
            slug="robot-logs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_collection = response.parse()
            assert_matches_type(UploadCollection, upload_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        upload_collection = client.upload_collections.retrieve(
            "upl_col_123",
        )
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.upload_collections.with_raw_response.retrieve(
            "upl_col_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_collection = response.parse()
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.upload_collections.with_streaming_response.retrieve(
            "upl_col_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_collection = response.parse()
            assert_matches_type(UploadCollection, upload_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_collection_id` but received ''"):
            client.upload_collections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Miru) -> None:
        upload_collection = client.upload_collections.update(
            upload_collection_id="upl_col_123",
        )
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Miru) -> None:
        upload_collection = client.upload_collections.update(
            upload_collection_id="upl_col_123",
            name="Robot Logs",
            slug="robot-logs",
        )
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Miru) -> None:
        response = client.upload_collections.with_raw_response.update(
            upload_collection_id="upl_col_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_collection = response.parse()
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Miru) -> None:
        with client.upload_collections.with_streaming_response.update(
            upload_collection_id="upl_col_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_collection = response.parse()
            assert_matches_type(UploadCollection, upload_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_collection_id` but received ''"):
            client.upload_collections.with_raw_response.update(
                upload_collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        upload_collection = client.upload_collections.list()
        assert_matches_type(UploadCollectionListResponse, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        upload_collection = client.upload_collections.list(
            id=["upl_col_123"],
            expand=["total_count"],
            limit=10,
            name=["Robot Logs"],
            offset=0,
            order_by=["created_at:desc"],
            slug=["robot-logs"],
        )
        assert_matches_type(UploadCollectionListResponse, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.upload_collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_collection = response.parse()
        assert_matches_type(UploadCollectionListResponse, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.upload_collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_collection = response.parse()
            assert_matches_type(UploadCollectionListResponse, upload_collection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUploadCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        upload_collection = await async_client.upload_collections.create(
            name="Robot Logs",
            slug="robot-logs",
        )
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.upload_collections.with_raw_response.create(
            name="Robot Logs",
            slug="robot-logs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_collection = await response.parse()
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.upload_collections.with_streaming_response.create(
            name="Robot Logs",
            slug="robot-logs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_collection = await response.parse()
            assert_matches_type(UploadCollection, upload_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        upload_collection = await async_client.upload_collections.retrieve(
            "upl_col_123",
        )
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.upload_collections.with_raw_response.retrieve(
            "upl_col_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_collection = await response.parse()
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.upload_collections.with_streaming_response.retrieve(
            "upl_col_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_collection = await response.parse()
            assert_matches_type(UploadCollection, upload_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_collection_id` but received ''"):
            await async_client.upload_collections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMiru) -> None:
        upload_collection = await async_client.upload_collections.update(
            upload_collection_id="upl_col_123",
        )
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMiru) -> None:
        upload_collection = await async_client.upload_collections.update(
            upload_collection_id="upl_col_123",
            name="Robot Logs",
            slug="robot-logs",
        )
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMiru) -> None:
        response = await async_client.upload_collections.with_raw_response.update(
            upload_collection_id="upl_col_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_collection = await response.parse()
        assert_matches_type(UploadCollection, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMiru) -> None:
        async with async_client.upload_collections.with_streaming_response.update(
            upload_collection_id="upl_col_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_collection = await response.parse()
            assert_matches_type(UploadCollection, upload_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_collection_id` but received ''"):
            await async_client.upload_collections.with_raw_response.update(
                upload_collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        upload_collection = await async_client.upload_collections.list()
        assert_matches_type(UploadCollectionListResponse, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        upload_collection = await async_client.upload_collections.list(
            id=["upl_col_123"],
            expand=["total_count"],
            limit=10,
            name=["Robot Logs"],
            offset=0,
            order_by=["created_at:desc"],
            slug=["robot-logs"],
        )
        assert_matches_type(UploadCollectionListResponse, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.upload_collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_collection = await response.parse()
        assert_matches_type(UploadCollectionListResponse, upload_collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.upload_collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_collection = await response.parse()
            assert_matches_type(UploadCollectionListResponse, upload_collection, path=["response"])

        assert cast(Any, response.is_closed) is True
