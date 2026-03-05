# ConfigInstances

Types:

```python
from miru_platform.types import (
    ConfigInstance,
    InstanceContent,
    PaginatedList,
    ConfigInstanceListResponse,
)
```

Methods:

- <code title="post /config_instances">client.config_instances.<a href="./src/miru_platform/resources/config_instances.py">create</a>(\*\*<a href="src/miru_platform/types/config_instance_create_params.py">params</a>) -> <a href="./src/miru_platform/types/config_instance.py">ConfigInstance</a></code>
- <code title="get /config_instances/{config_instance_id}">client.config_instances.<a href="./src/miru_platform/resources/config_instances.py">retrieve</a>(config_instance_id, \*\*<a href="src/miru_platform/types/config_instance_retrieve_params.py">params</a>) -> <a href="./src/miru_platform/types/config_instance.py">ConfigInstance</a></code>
- <code title="get /config_instances">client.config_instances.<a href="./src/miru_platform/resources/config_instances.py">list</a>(\*\*<a href="src/miru_platform/types/config_instance_list_params.py">params</a>) -> <a href="./src/miru_platform/types/config_instance_list_response.py">ConfigInstanceListResponse</a></code>
- <code title="get /config_instances/{config_instance_id}/content">client.config_instances.<a href="./src/miru_platform/resources/config_instances.py">download_content</a>(config_instance_id, \*\*<a href="src/miru_platform/types/config_instance_download_content_params.py">params</a>) -> BinaryAPIResponse</code>

# ConfigSchemas

Types:

```python
from miru_platform.types import ConfigSchema, ConfigSchemaList
```

Methods:

- <code title="post /config_schemas">client.config_schemas.<a href="./src/miru_platform/resources/config_schemas.py">create</a>(\*\*<a href="src/miru_platform/types/config_schema_create_params.py">params</a>) -> <a href="./src/miru_platform/types/config_schema.py">ConfigSchema</a></code>
- <code title="get /config_schemas/{config_schema_id}">client.config_schemas.<a href="./src/miru_platform/resources/config_schemas.py">retrieve</a>(config_schema_id, \*\*<a href="src/miru_platform/types/config_schema_retrieve_params.py">params</a>) -> <a href="./src/miru_platform/types/config_schema.py">ConfigSchema</a></code>
- <code title="get /config_schemas">client.config_schemas.<a href="./src/miru_platform/resources/config_schemas.py">list</a>(\*\*<a href="src/miru_platform/types/config_schema_list_params.py">params</a>) -> <a href="./src/miru_platform/types/config_schema_list.py">ConfigSchemaList</a></code>

# ConfigTypes

Types:

```python
from miru_platform.types import ConfigType, ConfigTypeListResponse
```

Methods:

- <code title="post /config_types">client.config_types.<a href="./src/miru_platform/resources/config_types.py">create</a>(\*\*<a href="src/miru_platform/types/config_type_create_params.py">params</a>) -> <a href="./src/miru_platform/types/config_type.py">ConfigType</a></code>
- <code title="get /config_types/{config_type_id}">client.config_types.<a href="./src/miru_platform/resources/config_types.py">retrieve</a>(config_type_id, \*\*<a href="src/miru_platform/types/config_type_retrieve_params.py">params</a>) -> <a href="./src/miru_platform/types/config_type.py">ConfigType</a></code>
- <code title="patch /config_types/{config_type_id}">client.config_types.<a href="./src/miru_platform/resources/config_types.py">update</a>(config_type_id, \*\*<a href="src/miru_platform/types/config_type_update_params.py">params</a>) -> <a href="./src/miru_platform/types/config_type.py">ConfigType</a></code>
- <code title="get /config_types">client.config_types.<a href="./src/miru_platform/resources/config_types.py">list</a>(\*\*<a href="src/miru_platform/types/config_type_list_params.py">params</a>) -> <a href="./src/miru_platform/types/config_type_list_response.py">ConfigTypeListResponse</a></code>

# Deployments

Types:

```python
from miru_platform.types import Deployment, DeploymentList
```

Methods:

- <code title="post /deployments">client.deployments.<a href="./src/miru_platform/resources/deployments.py">create</a>(\*\*<a href="src/miru_platform/types/deployment_create_params.py">params</a>) -> <a href="./src/miru_platform/types/deployment.py">Deployment</a></code>
- <code title="get /deployments/{deployment_id}">client.deployments.<a href="./src/miru_platform/resources/deployments.py">retrieve</a>(deployment_id, \*\*<a href="src/miru_platform/types/deployment_retrieve_params.py">params</a>) -> <a href="./src/miru_platform/types/deployment.py">Deployment</a></code>
- <code title="get /deployments">client.deployments.<a href="./src/miru_platform/resources/deployments.py">list</a>(\*\*<a href="src/miru_platform/types/deployment_list_params.py">params</a>) -> <a href="./src/miru_platform/types/deployment_list.py">DeploymentList</a></code>
- <code title="post /deployments/{deployment_id}/archive">client.deployments.<a href="./src/miru_platform/resources/deployments.py">archive</a>(deployment_id, \*\*<a href="src/miru_platform/types/deployment_archive_params.py">params</a>) -> <a href="./src/miru_platform/types/deployment.py">Deployment</a></code>
- <code title="post /deployments/{deployment_id}/deploy">client.deployments.<a href="./src/miru_platform/resources/deployments.py">deploy</a>(deployment_id, \*\*<a href="src/miru_platform/types/deployment_deploy_params.py">params</a>) -> <a href="./src/miru_platform/types/deployment.py">Deployment</a></code>
- <code title="get /deployments/{deployment_id}/drifts">client.deployments.<a href="./src/miru_platform/resources/deployments.py">list_drifts</a>(deployment_id, \*\*<a href="src/miru_platform/types/deployment_list_drifts_params.py">params</a>) -> <a href="./src/miru_platform/types/deployment_list.py">DeploymentList</a></code>

# Devices

Types:

```python
from miru_platform.types import (
    Device,
    DeviceListResponse,
    DeviceCreateActivationTokenResponse,
    DevicePingResponse,
)
```

Methods:

- <code title="post /devices">client.devices.<a href="./src/miru_platform/resources/devices.py">create</a>(\*\*<a href="src/miru_platform/types/device_create_params.py">params</a>) -> <a href="./src/miru_platform/types/device.py">Device</a></code>
- <code title="get /devices/{device_id}">client.devices.<a href="./src/miru_platform/resources/devices.py">retrieve</a>(device_id) -> <a href="./src/miru_platform/types/device.py">Device</a></code>
- <code title="patch /devices/{device_id}">client.devices.<a href="./src/miru_platform/resources/devices.py">update</a>(device_id, \*\*<a href="src/miru_platform/types/device_update_params.py">params</a>) -> <a href="./src/miru_platform/types/device.py">Device</a></code>
- <code title="get /devices">client.devices.<a href="./src/miru_platform/resources/devices.py">list</a>(\*\*<a href="src/miru_platform/types/device_list_params.py">params</a>) -> <a href="./src/miru_platform/types/device_list_response.py">DeviceListResponse</a></code>
- <code title="post /devices/{device_id}/activation_token">client.devices.<a href="./src/miru_platform/resources/devices.py">create_activation_token</a>(device_id, \*\*<a href="src/miru_platform/types/device_create_activation_token_params.py">params</a>) -> <a href="./src/miru_platform/types/device_create_activation_token_response.py">DeviceCreateActivationTokenResponse</a></code>
- <code title="post /devices/{device_id}/ping">client.devices.<a href="./src/miru_platform/resources/devices.py">ping</a>(device_id, \*\*<a href="src/miru_platform/types/device_ping_params.py">params</a>) -> <a href="./src/miru_platform/types/device_ping_response.py">DevicePingResponse</a></code>

# GitCommits

Types:

```python
from miru_platform.types import GitCommit, GitCommitListResponse
```

Methods:

- <code title="post /git_commits">client.git_commits.<a href="./src/miru_platform/resources/git_commits.py">create</a>(\*\*<a href="src/miru_platform/types/git_commit_create_params.py">params</a>) -> <a href="./src/miru_platform/types/git_commit.py">GitCommit</a></code>
- <code title="get /git_commits/{git_commit_id}">client.git_commits.<a href="./src/miru_platform/resources/git_commits.py">retrieve</a>(git_commit_id) -> <a href="./src/miru_platform/types/git_commit.py">GitCommit</a></code>
- <code title="get /git_commits">client.git_commits.<a href="./src/miru_platform/resources/git_commits.py">list</a>(\*\*<a href="src/miru_platform/types/git_commit_list_params.py">params</a>) -> <a href="./src/miru_platform/types/git_commit_list_response.py">GitCommitListResponse</a></code>

# Principal

Types:

```python
from miru_platform.types import PrincipalIdentifyResponse
```

Methods:

- <code title="get /principal">client.principal.<a href="./src/miru_platform/resources/principal.py">identify</a>() -> <a href="./src/miru_platform/types/principal_identify_response.py">PrincipalIdentifyResponse</a></code>

# Releases

Types:

```python
from miru_platform.types import GitCommitRef, Release, ReleaseListResponse
```

Methods:

- <code title="post /releases">client.releases.<a href="./src/miru_platform/resources/releases.py">create</a>(\*\*<a href="src/miru_platform/types/release_create_params.py">params</a>) -> <a href="./src/miru_platform/types/release.py">Release</a></code>
- <code title="get /releases/{release_id}">client.releases.<a href="./src/miru_platform/resources/releases.py">retrieve</a>(release_id, \*\*<a href="src/miru_platform/types/release_retrieve_params.py">params</a>) -> <a href="./src/miru_platform/types/release.py">Release</a></code>
- <code title="get /releases">client.releases.<a href="./src/miru_platform/resources/releases.py">list</a>(\*\*<a href="src/miru_platform/types/release_list_params.py">params</a>) -> <a href="./src/miru_platform/types/release_list_response.py">ReleaseListResponse</a></code>
