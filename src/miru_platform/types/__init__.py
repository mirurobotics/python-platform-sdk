# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import release, deployment, config_type, config_schema, config_instance
from .. import _compat
from .device import Device as Device
from .release import Release as Release
from .deployment import Deployment as Deployment
from .git_commit import GitCommit as GitCommit
from .config_type import ConfigType as ConfigType
from .config_schema import ConfigSchema as ConfigSchema
from .paginated_list import PaginatedList as PaginatedList
from .config_instance import ConfigInstance as ConfigInstance
from .deployment_list import DeploymentList as DeploymentList
from .instance_content import InstanceContent as InstanceContent
from .config_schema_list import ConfigSchemaList as ConfigSchemaList
from .device_list_params import DeviceListParams as DeviceListParams
from .device_ping_params import DevicePingParams as DevicePingParams
from .release_list_params import ReleaseListParams as ReleaseListParams
from .device_create_params import DeviceCreateParams as DeviceCreateParams
from .device_list_response import DeviceListResponse as DeviceListResponse
from .device_ping_response import DevicePingResponse as DevicePingResponse
from .device_update_params import DeviceUpdateParams as DeviceUpdateParams
from .git_commit_ref_param import GitCommitRefParam as GitCommitRefParam
from .release_create_params import ReleaseCreateParams as ReleaseCreateParams
from .release_list_response import ReleaseListResponse as ReleaseListResponse
from .deployment_list_params import DeploymentListParams as DeploymentListParams
from .git_commit_list_params import GitCommitListParams as GitCommitListParams
from .instance_content_param import InstanceContentParam as InstanceContentParam
from .config_type_list_params import ConfigTypeListParams as ConfigTypeListParams
from .release_retrieve_params import ReleaseRetrieveParams as ReleaseRetrieveParams
from .deployment_create_params import DeploymentCreateParams as DeploymentCreateParams
from .deployment_deploy_params import DeploymentDeployParams as DeploymentDeployParams
from .git_commit_create_params import GitCommitCreateParams as GitCommitCreateParams
from .git_commit_list_response import GitCommitListResponse as GitCommitListResponse
from .config_schema_list_params import ConfigSchemaListParams as ConfigSchemaListParams
from .config_type_create_params import ConfigTypeCreateParams as ConfigTypeCreateParams
from .config_type_list_response import ConfigTypeListResponse as ConfigTypeListResponse
from .config_type_update_params import ConfigTypeUpdateParams as ConfigTypeUpdateParams
from .deployment_archive_params import DeploymentArchiveParams as DeploymentArchiveParams
from .deployment_retrieve_params import DeploymentRetrieveParams as DeploymentRetrieveParams
from .config_instance_list_params import ConfigInstanceListParams as ConfigInstanceListParams
from .config_schema_create_params import ConfigSchemaCreateParams as ConfigSchemaCreateParams
from .config_type_retrieve_params import ConfigTypeRetrieveParams as ConfigTypeRetrieveParams
from .principal_identify_response import PrincipalIdentifyResponse as PrincipalIdentifyResponse
from .config_instance_create_params import ConfigInstanceCreateParams as ConfigInstanceCreateParams
from .config_instance_list_response import ConfigInstanceListResponse as ConfigInstanceListResponse
from .config_schema_retrieve_params import ConfigSchemaRetrieveParams as ConfigSchemaRetrieveParams
from .deployment_list_drifts_params import DeploymentListDriftsParams as DeploymentListDriftsParams
from .config_instance_retrieve_params import ConfigInstanceRetrieveParams as ConfigInstanceRetrieveParams
from .device_create_activation_token_params import (
    DeviceCreateActivationTokenParams as DeviceCreateActivationTokenParams,
)
from .config_instance_download_content_params import (
    ConfigInstanceDownloadContentParams as ConfigInstanceDownloadContentParams,
)
from .device_create_activation_token_response import (
    DeviceCreateActivationTokenResponse as DeviceCreateActivationTokenResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    config_instance.ConfigInstance.update_forward_refs()  # type: ignore
    config_schema.ConfigSchema.update_forward_refs()  # type: ignore
    config_type.ConfigType.update_forward_refs()  # type: ignore
    deployment.Deployment.update_forward_refs()  # type: ignore
    release.Release.update_forward_refs()  # type: ignore
else:
    config_instance.ConfigInstance.model_rebuild(_parent_namespace_depth=0)
    config_schema.ConfigSchema.model_rebuild(_parent_namespace_depth=0)
    config_type.ConfigType.model_rebuild(_parent_namespace_depth=0)
    deployment.Deployment.model_rebuild(_parent_namespace_depth=0)
    release.Release.model_rebuild(_parent_namespace_depth=0)
