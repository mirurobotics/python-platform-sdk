# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    deployment_list_params,
    deployment_create_params,
    deployment_deploy_params,
    deployment_archive_params,
    deployment_retrieve_params,
    deployment_list_drifts_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.deployment import Deployment
from ..types.deployment_list import DeploymentList

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return DeploymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config_instance_ids: SequenceNotStr[str],
        description: str,
        device_id: str,
        release_id: str,
        target_status: Literal["staged", "deployed"],
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Stage or deploy a new deployment.

        Args:
          config_instance_ids: The IDs of the config instances to deploy. A deployment must have exactly one
              config instance for each config schema in the deployment's release.

          description: The description of the deployment.

          device_id: The ID of the device that the deployment is being created for.

          release_id: The release ID which this deployment adheres to.

          target_status: Desired state of the deployment.

              - Staged: ready for deployment. Deployments can only be staged if their release
                is not the current release for the device.
              - Deployed: deployed to the device. Deployments can only be deployed if their
                release is the device's current release.

          expand: Fields to expand on the deployment resource.

          parent_id: The ID of the deployment that this deployment was patched from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/deployments",
            body=maybe_transform(
                {
                    "config_instance_ids": config_instance_ids,
                    "description": description,
                    "device_id": device_id,
                    "release_id": release_id,
                    "target_status": target_status,
                    "parent_id": parent_id,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, deployment_create_params.DeploymentCreateParams),
            ),
            cast_to=Deployment,
        )

    def retrieve(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Retrieve a deployment by its ID.

        Args:
          expand: Fields to expand on the deployment resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            path_template("/deployments/{deployment_id}", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, deployment_retrieve_params.DeploymentRetrieveParams),
            ),
            cast_to=Deployment,
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        activity_status: List[Literal["drifted", "staged", "queued", "deployed", "archived"]] | Omit = omit,
        device_id: SequenceNotStr[str] | Omit = omit,
        error_status: List[Literal["none", "failed", "retrying"]] | Omit = omit,
        expand: List[Literal["total_count", "device", "release", "config_instances"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        release_id: SequenceNotStr[str] | Omit = omit,
        target_status: List[Literal["staged", "deployed", "archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentList:
        """
        List all deployments.

        Args:
          id: The deployment IDs to filter by.

          activity_status: The deployment activity statuses to filter by.

          device_id: The deployment device IDs to filter by.

          error_status: The deployment error statuses to filter by.

          expand: Fields to expand on each deployment in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the deployment results.

          release_id: The deployment release IDs to filter by.

          target_status: The deployment target statuses to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "activity_status": activity_status,
                        "device_id": device_id,
                        "error_status": error_status,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "release_id": release_id,
                        "target_status": target_status,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            cast_to=DeploymentList,
        )

    def archive(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Archive staged or drifted deployments.

        Args:
          expand: Fields to expand on the deployment resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._post(
            path_template("/deployments/{deployment_id}/archive", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, deployment_archive_params.DeploymentArchiveParams),
            ),
            cast_to=Deployment,
        )

    def deploy(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Trigger a deployment to its target device.

        Args:
          expand: Fields to expand on the deployment resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._post(
            path_template("/deployments/{deployment_id}/deploy", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, deployment_deploy_params.DeploymentDeployParams),
            ),
            cast_to=Deployment,
        )

    def list_drifts(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentList:
        """
        List the deployments which have been deployed since this deployment was staged.

        Args:
          expand: Fields to expand on the deployment resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            path_template("/deployments/{deployment_id}/drifts", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, deployment_list_drifts_params.DeploymentListDriftsParams),
            ),
            cast_to=DeploymentList,
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-platform-sdk#with_streaming_response
        """
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config_instance_ids: SequenceNotStr[str],
        description: str,
        device_id: str,
        release_id: str,
        target_status: Literal["staged", "deployed"],
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Stage or deploy a new deployment.

        Args:
          config_instance_ids: The IDs of the config instances to deploy. A deployment must have exactly one
              config instance for each config schema in the deployment's release.

          description: The description of the deployment.

          device_id: The ID of the device that the deployment is being created for.

          release_id: The release ID which this deployment adheres to.

          target_status: Desired state of the deployment.

              - Staged: ready for deployment. Deployments can only be staged if their release
                is not the current release for the device.
              - Deployed: deployed to the device. Deployments can only be deployed if their
                release is the device's current release.

          expand: Fields to expand on the deployment resource.

          parent_id: The ID of the deployment that this deployment was patched from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/deployments",
            body=await async_maybe_transform(
                {
                    "config_instance_ids": config_instance_ids,
                    "description": description,
                    "device_id": device_id,
                    "release_id": release_id,
                    "target_status": target_status,
                    "parent_id": parent_id,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, deployment_create_params.DeploymentCreateParams),
            ),
            cast_to=Deployment,
        )

    async def retrieve(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Retrieve a deployment by its ID.

        Args:
          expand: Fields to expand on the deployment resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            path_template("/deployments/{deployment_id}", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, deployment_retrieve_params.DeploymentRetrieveParams
                ),
            ),
            cast_to=Deployment,
        )

    async def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        activity_status: List[Literal["drifted", "staged", "queued", "deployed", "archived"]] | Omit = omit,
        device_id: SequenceNotStr[str] | Omit = omit,
        error_status: List[Literal["none", "failed", "retrying"]] | Omit = omit,
        expand: List[Literal["total_count", "device", "release", "config_instances"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[Literal["id:asc", "id:desc", "created_at:desc", "created_at:asc"]] | Omit = omit,
        release_id: SequenceNotStr[str] | Omit = omit,
        target_status: List[Literal["staged", "deployed", "archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentList:
        """
        List all deployments.

        Args:
          id: The deployment IDs to filter by.

          activity_status: The deployment activity statuses to filter by.

          device_id: The deployment device IDs to filter by.

          error_status: The deployment error statuses to filter by.

          expand: Fields to expand on each deployment in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the deployment results.

          release_id: The deployment release IDs to filter by.

          target_status: The deployment target statuses to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "activity_status": activity_status,
                        "device_id": device_id,
                        "error_status": error_status,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "release_id": release_id,
                        "target_status": target_status,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            cast_to=DeploymentList,
        )

    async def archive(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Archive staged or drifted deployments.

        Args:
          expand: Fields to expand on the deployment resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._post(
            path_template("/deployments/{deployment_id}/archive", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, deployment_archive_params.DeploymentArchiveParams
                ),
            ),
            cast_to=Deployment,
        )

    async def deploy(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Trigger a deployment to its target device.

        Args:
          expand: Fields to expand on the deployment resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._post(
            path_template("/deployments/{deployment_id}/deploy", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, deployment_deploy_params.DeploymentDeployParams),
            ),
            cast_to=Deployment,
        )

    async def list_drifts(
        self,
        deployment_id: str,
        *,
        expand: List[Literal["device", "release", "config_instances"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeploymentList:
        """
        List the deployments which have been deployed since this deployment was staged.

        Args:
          expand: Fields to expand on the deployment resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            path_template("/deployments/{deployment_id}/drifts", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, deployment_list_drifts_params.DeploymentListDriftsParams
                ),
            ),
            cast_to=DeploymentList,
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_raw_response_wrapper(
            deployments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deployments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            deployments.list,
        )
        self.archive = to_raw_response_wrapper(
            deployments.archive,
        )
        self.deploy = to_raw_response_wrapper(
            deployments.deploy,
        )
        self.list_drifts = to_raw_response_wrapper(
            deployments.list_drifts,
        )


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_raw_response_wrapper(
            deployments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deployments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            deployments.list,
        )
        self.archive = async_to_raw_response_wrapper(
            deployments.archive,
        )
        self.deploy = async_to_raw_response_wrapper(
            deployments.deploy,
        )
        self.list_drifts = async_to_raw_response_wrapper(
            deployments.list_drifts,
        )


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_streamed_response_wrapper(
            deployments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deployments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            deployments.list,
        )
        self.archive = to_streamed_response_wrapper(
            deployments.archive,
        )
        self.deploy = to_streamed_response_wrapper(
            deployments.deploy,
        )
        self.list_drifts = to_streamed_response_wrapper(
            deployments.list_drifts,
        )


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_streamed_response_wrapper(
            deployments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deployments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            deployments.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            deployments.archive,
        )
        self.deploy = async_to_streamed_response_wrapper(
            deployments.deploy,
        )
        self.list_drifts = async_to_streamed_response_wrapper(
            deployments.list_drifts,
        )
