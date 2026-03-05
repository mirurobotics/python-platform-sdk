# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_platform import MiruPlatform, AsyncMiruPlatform
from miru_platform.types import GitCommit, GitCommitListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGitCommits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: MiruPlatform) -> None:
        git_commit = client.git_commits.create(
            message="Update config schema for robot1",
            origin="https://github.com/robot1/robot1.git",
            sha="a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(GitCommit, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: MiruPlatform) -> None:
        response = client.git_commits.with_raw_response.create(
            message="Update config schema for robot1",
            origin="https://github.com/robot1/robot1.git",
            sha="a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_commit = response.parse()
        assert_matches_type(GitCommit, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: MiruPlatform) -> None:
        with client.git_commits.with_streaming_response.create(
            message="Update config schema for robot1",
            origin="https://github.com/robot1/robot1.git",
            sha="a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_commit = response.parse()
            assert_matches_type(GitCommit, git_commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: MiruPlatform) -> None:
        git_commit = client.git_commits.retrieve(
            git_commit_id="git_commit_123",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(GitCommit, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: MiruPlatform) -> None:
        response = client.git_commits.with_raw_response.retrieve(
            git_commit_id="git_commit_123",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_commit = response.parse()
        assert_matches_type(GitCommit, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: MiruPlatform) -> None:
        with client.git_commits.with_streaming_response.retrieve(
            git_commit_id="git_commit_123",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_commit = response.parse()
            assert_matches_type(GitCommit, git_commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: MiruPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `git_commit_id` but received ''"):
            client.git_commits.with_raw_response.retrieve(
                git_commit_id="",
                miru_version="2026-03-09.tetons",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: MiruPlatform) -> None:
        git_commit = client.git_commits.list(
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(GitCommitListResponse, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: MiruPlatform) -> None:
        git_commit = client.git_commits.list(
            miru_version="2026-03-09.tetons",
            id=["git_cmt_123"],
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by=["id:asc"],
            sha=["a1b2c3d4e5f6"],
        )
        assert_matches_type(GitCommitListResponse, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: MiruPlatform) -> None:
        response = client.git_commits.with_raw_response.list(
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_commit = response.parse()
        assert_matches_type(GitCommitListResponse, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: MiruPlatform) -> None:
        with client.git_commits.with_streaming_response.list(
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_commit = response.parse()
            assert_matches_type(GitCommitListResponse, git_commit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGitCommits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiruPlatform) -> None:
        git_commit = await async_client.git_commits.create(
            message="Update config schema for robot1",
            origin="https://github.com/robot1/robot1.git",
            sha="a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(GitCommit, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.git_commits.with_raw_response.create(
            message="Update config schema for robot1",
            origin="https://github.com/robot1/robot1.git",
            sha="a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_commit = await response.parse()
        assert_matches_type(GitCommit, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.git_commits.with_streaming_response.create(
            message="Update config schema for robot1",
            origin="https://github.com/robot1/robot1.git",
            sha="a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_commit = await response.parse()
            assert_matches_type(GitCommit, git_commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        git_commit = await async_client.git_commits.retrieve(
            git_commit_id="git_commit_123",
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(GitCommit, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.git_commits.with_raw_response.retrieve(
            git_commit_id="git_commit_123",
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_commit = await response.parse()
        assert_matches_type(GitCommit, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.git_commits.with_streaming_response.retrieve(
            git_commit_id="git_commit_123",
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_commit = await response.parse()
            assert_matches_type(GitCommit, git_commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiruPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `git_commit_id` but received ''"):
            await async_client.git_commits.with_raw_response.retrieve(
                git_commit_id="",
                miru_version="2026-03-09.tetons",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiruPlatform) -> None:
        git_commit = await async_client.git_commits.list(
            miru_version="2026-03-09.tetons",
        )
        assert_matches_type(GitCommitListResponse, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiruPlatform) -> None:
        git_commit = await async_client.git_commits.list(
            miru_version="2026-03-09.tetons",
            id=["git_cmt_123"],
            expand=["total_count"],
            limit=1,
            offset=0,
            order_by=["id:asc"],
            sha=["a1b2c3d4e5f6"],
        )
        assert_matches_type(GitCommitListResponse, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiruPlatform) -> None:
        response = await async_client.git_commits.with_raw_response.list(
            miru_version="2026-03-09.tetons",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git_commit = await response.parse()
        assert_matches_type(GitCommitListResponse, git_commit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiruPlatform) -> None:
        async with async_client.git_commits.with_streaming_response.list(
            miru_version="2026-03-09.tetons",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git_commit = await response.parse()
            assert_matches_type(GitCommitListResponse, git_commit, path=["response"])

        assert cast(Any, response.is_closed) is True
