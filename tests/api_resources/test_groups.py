# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform_sdk import Miru, AsyncMiru
from miru_platform_sdk.types import (
    Group,
    GroupList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        group = client.groups.create(
            name="Robots",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Miru) -> None:
        group = client.groups.create(
            name="Robots",
            expand=["parent"],
            parent_id="grp_456",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.groups.with_raw_response.create(
            name="Robots",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.groups.with_streaming_response.create(
            name="Robots",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Group, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        group = client.groups.retrieve(
            group_id="grp_123",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        group = client.groups.retrieve(
            group_id="grp_123",
            expand=["parent"],
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.groups.with_raw_response.retrieve(
            group_id="grp_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.groups.with_streaming_response.retrieve(
            group_id="grp_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Group, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.groups.with_raw_response.retrieve(
                group_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Miru) -> None:
        group = client.groups.update(
            group_id="grp_123",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Miru) -> None:
        group = client.groups.update(
            group_id="grp_123",
            expand=["parent"],
            name="Robots",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Miru) -> None:
        response = client.groups.with_raw_response.update(
            group_id="grp_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Miru) -> None:
        with client.groups.with_streaming_response.update(
            group_id="grp_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Group, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.groups.with_raw_response.update(
                group_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        group = client.groups.list()
        assert_matches_type(GroupList, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        group = client.groups.list(
            id=["grp_123"],
            expand=["parent"],
            limit=10,
            name=["production"],
            offset=0,
            order_by=["created_at:desc"],
            parent_id=["grp_456"],
        )
        assert_matches_type(GroupList, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupList, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupList, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_move(self, client: Miru) -> None:
        group = client.groups.move(
            group_id="grp_123",
            parent_id="grp_456",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_move_with_all_params(self, client: Miru) -> None:
        group = client.groups.move(
            group_id="grp_123",
            parent_id="grp_456",
            expand=["parent"],
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_move(self, client: Miru) -> None:
        response = client.groups.with_raw_response.move(
            group_id="grp_123",
            parent_id="grp_456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_move(self, client: Miru) -> None:
        with client.groups.with_streaming_response.move(
            group_id="grp_123",
            parent_id="grp_456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(Group, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_move(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.groups.with_raw_response.move(
                group_id="",
                parent_id="grp_456",
            )


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.create(
            name="Robots",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.create(
            name="Robots",
            expand=["parent"],
            parent_id="grp_456",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.groups.with_raw_response.create(
            name="Robots",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.groups.with_streaming_response.create(
            name="Robots",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Group, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.retrieve(
            group_id="grp_123",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.retrieve(
            group_id="grp_123",
            expand=["parent"],
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.groups.with_raw_response.retrieve(
            group_id="grp_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.groups.with_streaming_response.retrieve(
            group_id="grp_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Group, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.groups.with_raw_response.retrieve(
                group_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.update(
            group_id="grp_123",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.update(
            group_id="grp_123",
            expand=["parent"],
            name="Robots",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMiru) -> None:
        response = await async_client.groups.with_raw_response.update(
            group_id="grp_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMiru) -> None:
        async with async_client.groups.with_streaming_response.update(
            group_id="grp_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Group, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.groups.with_raw_response.update(
                group_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.list()
        assert_matches_type(GroupList, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.list(
            id=["grp_123"],
            expand=["parent"],
            limit=10,
            name=["production"],
            offset=0,
            order_by=["created_at:desc"],
            parent_id=["grp_456"],
        )
        assert_matches_type(GroupList, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupList, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupList, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_move(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.move(
            group_id="grp_123",
            parent_id="grp_456",
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_move_with_all_params(self, async_client: AsyncMiru) -> None:
        group = await async_client.groups.move(
            group_id="grp_123",
            parent_id="grp_456",
            expand=["parent"],
        )
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_move(self, async_client: AsyncMiru) -> None:
        response = await async_client.groups.with_raw_response.move(
            group_id="grp_123",
            parent_id="grp_456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(Group, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncMiru) -> None:
        async with async_client.groups.with_streaming_response.move(
            group_id="grp_123",
            parent_id="grp_456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(Group, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_move(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.groups.with_raw_response.move(
                group_id="",
                parent_id="grp_456",
            )
