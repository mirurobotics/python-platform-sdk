# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import group, device, component, deployment, component_role, component_aspect
from .. import _compat
from .group import Group as Group
from .device import Device as Device
from .shared import PaginatedList as PaginatedList
from .release import Release as Release
from .component import Component as Component
from .principal import Principal as Principal
from .deployment import Deployment as Deployment
from .git_commit import GitCommit as GitCommit
from .group_list import GroupList as GroupList
from .calibration import Calibration as Calibration
from .config_type import ConfigType as ConfigType
from .device_list import DeviceList as DeviceList
from .release_list import ReleaseList as ReleaseList
from .config_schema import ConfigSchema as ConfigSchema
from .instance_slot import InstanceSlot as InstanceSlot
from .component_list import ComponentList as ComponentList
from .component_role import ComponentRole as ComponentRole
from .config_instance import ConfigInstance as ConfigInstance
from .deployment_list import DeploymentList as DeploymentList
from .git_commit_list import GitCommitList as GitCommitList
from .schema_document import SchemaDocument as SchemaDocument
from .schema_language import SchemaLanguage as SchemaLanguage
from .calibration_list import CalibrationList as CalibrationList
from .component_aspect import ComponentAspect as ComponentAspect
from .instance_content import InstanceContent as InstanceContent
from .group_list_params import GroupListParams as GroupListParams
from .group_move_params import GroupMoveParams as GroupMoveParams
from .config_schema_list import ConfigSchemaList as ConfigSchemaList
from .device_list_params import DeviceListParams as DeviceListParams
from .device_ping_params import DevicePingParams as DevicePingParams
from .provisioning_token import ProvisioningToken as ProvisioningToken
from .component_role_list import ComponentRoleList as ComponentRoleList
from .group_create_params import GroupCreateParams as GroupCreateParams
from .group_update_params import GroupUpdateParams as GroupUpdateParams
from .instance_slot_param import InstanceSlotParam as InstanceSlotParam
from .release_list_params import ReleaseListParams as ReleaseListParams
from .device_create_params import DeviceCreateParams as DeviceCreateParams
from .device_ping_response import DevicePingResponse as DevicePingResponse
from .device_update_params import DeviceUpdateParams as DeviceUpdateParams
from .git_commit_ref_param import GitCommitRefParam as GitCommitRefParam
from .component_aspect_list import ComponentAspectList as ComponentAspectList
from .component_list_params import ComponentListParams as ComponentListParams
from .group_retrieve_params import GroupRetrieveParams as GroupRetrieveParams
from .release_create_params import ReleaseCreateParams as ReleaseCreateParams
from .deployment_list_params import DeploymentListParams as DeploymentListParams
from .device_retrieve_params import DeviceRetrieveParams as DeviceRetrieveParams
from .git_commit_list_params import GitCommitListParams as GitCommitListParams
from .instance_content_param import InstanceContentParam as InstanceContentParam
from .calibration_list_params import CalibrationListParams as CalibrationListParams
from .config_type_list_params import ConfigTypeListParams as ConfigTypeListParams
from .release_retrieve_params import ReleaseRetrieveParams as ReleaseRetrieveParams
from .deployment_create_params import DeploymentCreateParams as DeploymentCreateParams
from .deployment_deploy_params import DeploymentDeployParams as DeploymentDeployParams
from .git_commit_create_params import GitCommitCreateParams as GitCommitCreateParams
from .component_retrieve_params import ComponentRetrieveParams as ComponentRetrieveParams
from .config_schema_list_params import ConfigSchemaListParams as ConfigSchemaListParams
from .config_type_create_params import ConfigTypeCreateParams as ConfigTypeCreateParams
from .config_type_list_response import ConfigTypeListResponse as ConfigTypeListResponse
from .config_type_update_params import ConfigTypeUpdateParams as ConfigTypeUpdateParams
from .deployment_archive_params import DeploymentArchiveParams as DeploymentArchiveParams
from .component_role_list_params import ComponentRoleListParams as ComponentRoleListParams
from .deployment_retrieve_params import DeploymentRetrieveParams as DeploymentRetrieveParams
from .calibration_retrieve_params import CalibrationRetrieveParams as CalibrationRetrieveParams
from .config_instance_list_params import ConfigInstanceListParams as ConfigInstanceListParams
from .config_schema_create_params import ConfigSchemaCreateParams as ConfigSchemaCreateParams
from .component_aspect_list_params import ComponentAspectListParams as ComponentAspectListParams
from .config_instance_create_params import ConfigInstanceCreateParams as ConfigInstanceCreateParams
from .config_instance_list_response import ConfigInstanceListResponse as ConfigInstanceListResponse
from .config_schema_retrieve_params import ConfigSchemaRetrieveParams as ConfigSchemaRetrieveParams
from .deployment_list_drifts_params import DeploymentListDriftsParams as DeploymentListDriftsParams
from .component_role_retrieve_params import ComponentRoleRetrieveParams as ComponentRoleRetrieveParams
from .config_instance_download_params import ConfigInstanceDownloadParams as ConfigInstanceDownloadParams
from .config_instance_retrieve_params import ConfigInstanceRetrieveParams as ConfigInstanceRetrieveParams
from .component_aspect_retrieve_params import ComponentAspectRetrieveParams as ComponentAspectRetrieveParams

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    component.Component.update_forward_refs()  # type: ignore
    component_aspect.ComponentAspect.update_forward_refs()  # type: ignore
    component_role.ComponentRole.update_forward_refs()  # type: ignore
    deployment.Deployment.update_forward_refs()  # type: ignore
    device.Device.update_forward_refs()  # type: ignore
    group.Group.update_forward_refs()  # type: ignore
else:
    component.Component.model_rebuild(_parent_namespace_depth=0)
    component_aspect.ComponentAspect.model_rebuild(_parent_namespace_depth=0)
    component_role.ComponentRole.model_rebuild(_parent_namespace_depth=0)
    deployment.Deployment.model_rebuild(_parent_namespace_depth=0)
    device.Device.model_rebuild(_parent_namespace_depth=0)
    group.Group.model_rebuild(_parent_namespace_depth=0)
