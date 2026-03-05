# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform import MiruPlatform, AsyncMiruPlatform
from miru_platform.types import (
    ConfigSchema,
    ConfigSchemaList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: MiruPlatform) -> None:
        config_schema = client.config_schemas.create(
            config_type_ref={},
            documents=[
                {
                    "data": "data",
                    "name": "motion-control.json",
                }
            ],
            format="json",
            language="jsonschema",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: MiruPlatform) -> None:
        config_schema = client.config_schemas.create(
            config_type_ref={
                "id": "cfg_123",
                "slug": "my-config-type",
            },
            documents=[
                {
                    "data": "data",
                    "name": "motion-control.json",
                }
            ],
            format="json",
            language="jsonschema",
            miru_version="2026-03-09.tetons",
            expand=["documents"],
            git_commit={
                "commit_ref": {
                    "id": "git_cmt_123",
                    "sha": "1a2b3c4d...",
                },
                "schema_filepaths": ["path/to/config/schema/robot1.cue", "path/to/config/schema/robot2.cue"],
            },
            instance_filepath="/v1/motion-control.json",
        )
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: MiruPlatform) -> None:
        response = client.config_schemas.with_raw_response.create(
            config_type_ref={},
            documents=[
                {
                    "data": "data",
                    "name": "motion-control.json",
                }
            ],
            format="json",
            language="jsonschema",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_schema = response.parse()
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: MiruPlatform) -> None:
        with client.config_schemas.with_streaming_response.create(
            config_type_ref={},
            documents=[
                {
                    "data": "data",
                    "name": "motion-control.json",
                }
            ],
            format="json",
            language="jsonschema",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_schema = response.parse()
            assert_matches_type(ConfigSchema, config_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: MiruPlatform) -> None:
        config_schema = client.config_schemas.retrieve(
            config_schema_id="cfg_sch_123",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: MiruPlatform) -> None:
        config_schema = client.config_schemas.retrieve(
            config_schema_id="cfg_sch_123",
            miru_version="2026-03-09.tetons",
            expand=["documents"],
        )
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: MiruPlatform) -> None:
        response = client.config_schemas.with_raw_response.retrieve(
            config_schema_id="cfg_sch_123",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_schema = response.parse()
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: MiruPlatform) -> None:
        with client.config_schemas.with_streaming_response.retrieve(
            config_schema_id="cfg_sch_123",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_schema = response.parse()
            assert_matches_type(ConfigSchema, config_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: MiruPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_schema_id` but received ''"):
            client.config_schemas.with_raw_response.retrieve(
                config_schema_id="",
                miru_version="2026-03-09.tetons",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: MiruPlatform) -> None:
        config_schema = client.config_schemas.list(
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(ConfigSchemaList, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: MiruPlatform) -> None:
        config_schema = client.config_schemas.list(
            miru_version="2026-03-09.tetons",
            id=["cfg_sch_123"],
            config_type_id=["cfg_typ_123"],
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by=["id:asc"],
        )
        assert_matches_type(ConfigSchemaList, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: MiruPlatform) -> None:
        response = client.config_schemas.with_raw_response.list(
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_schema = response.parse()
        assert_matches_type(ConfigSchemaList, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: MiruPlatform) -> None:
        with client.config_schemas.with_streaming_response.list(
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_schema = response.parse()
            assert_matches_type(ConfigSchemaList, config_schema, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigSchemas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiruPlatform) -> None:
        config_schema = await async_client.config_schemas.create(
            config_type_ref={},
            documents=[
                {
                    "data": "data",
                    "name": "motion-control.json",
                }
            ],
            format="json",
            language="jsonschema",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMiruPlatform) -> None:
        config_schema = await async_client.config_schemas.create(
            config_type_ref={
                "id": "cfg_123",
                "slug": "my-config-type",
            },
            documents=[
                {
                    "data": "data",
                    "name": "motion-control.json",
                }
            ],
            format="json",
            language="jsonschema",
            miru_version="2026-03-09.tetons",
            expand=["documents"],
            git_commit={
                "commit_ref": {
                    "id": "git_cmt_123",
                    "sha": "1a2b3c4d...",
                },
                "schema_filepaths": ["path/to/config/schema/robot1.cue", "path/to/config/schema/robot2.cue"],
            },
            instance_filepath="/v1/motion-control.json",
        )
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.config_schemas.with_raw_response.create(
            config_type_ref={},
            documents=[
                {
                    "data": "data",
                    "name": "motion-control.json",
                }
            ],
            format="json",
            language="jsonschema",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_schema = await response.parse()
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.config_schemas.with_streaming_response.create(
            config_type_ref={},
            documents=[
                {
                    "data": "data",
                    "name": "motion-control.json",
                }
            ],
            format="json",
            language="jsonschema",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_schema = await response.parse()
            assert_matches_type(ConfigSchema, config_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        config_schema = await async_client.config_schemas.retrieve(
            config_schema_id="cfg_sch_123",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiruPlatform) -> None:
        config_schema = await async_client.config_schemas.retrieve(
            config_schema_id="cfg_sch_123",
            miru_version="2026-03-09.tetons",
            expand=["documents"],
        )
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.config_schemas.with_raw_response.retrieve(
            config_schema_id="cfg_sch_123",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_schema = await response.parse()
        assert_matches_type(ConfigSchema, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.config_schemas.with_streaming_response.retrieve(
            config_schema_id="cfg_sch_123",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_schema = await response.parse()
            assert_matches_type(ConfigSchema, config_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_schema_id` but received ''"):
            await async_client.config_schemas.with_raw_response.retrieve(
                config_schema_id="",
                miru_version="2026-03-09.tetons",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiruPlatform) -> None:
        config_schema = await async_client.config_schemas.list(
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(ConfigSchemaList, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiruPlatform) -> None:
        config_schema = await async_client.config_schemas.list(
            miru_version="2026-03-09.tetons",
            id=["cfg_sch_123"],
            config_type_id=["cfg_typ_123"],
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by=["id:asc"],
        )
        assert_matches_type(ConfigSchemaList, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.config_schemas.with_raw_response.list(
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_schema = await response.parse()
        assert_matches_type(ConfigSchemaList, config_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.config_schemas.with_streaming_response.list(
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_schema = await response.parse()
            assert_matches_type(ConfigSchemaList, config_schema, path=["response"])

        assert cast(Any, response.is_closed) is True
