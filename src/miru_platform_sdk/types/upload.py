# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .upload_status import UploadStatus

__all__ = ["Upload", "Destination", "Source"]


class Destination(BaseModel):
    """Destination-side details of where an upload was written."""

    bucket_id: str
    """ID of the registered bucket the file was uploaded to."""

    bucket_name: str
    """Physical name of the bucket in the object store.

    This is the bucket parameter the device passes to the native cloud SDK (not the
    Miru `bucket_id`).
    """

    object_key: str
    """The object path the file was written to in the destination bucket."""


class Source(BaseModel):
    """Source-side details of the file on the device that produced an upload."""

    file_path: str
    """Absolute path of the file on the device.

    Its basename renders the `{file_name}` token in the upload path template.
    """

    first_observed_at: datetime
    """Timestamp of when the device agent first observed the file on the device."""

    last_observed_at: datetime
    """
    Timestamp of when the device agent most recently observed the file before the
    upload was minted.
    """

    mtime: datetime
    """The file's last-modified time (mtime) on the device, i.e.

    roughly when writing finished. In a create-upload request the agent sends it
    with the device's local UTC offset at that instant (e.g.
    `2021-01-01T00:00:00-05:00`), which a rule with `upload.timezone: device`
    renders its path's time variables in; older agents send UTC. Responses return it
    in UTC.
    """


class Upload(BaseModel):
    id: str
    """ID of the upload."""

    bundle_id: Optional[str] = None
    """ID of the bundle this upload belongs to.

    Null when the producing file rule does not bundle.
    """

    created_at: datetime
    """Timestamp of when the upload was created."""

    deployment_id: str
    """
    ID of the deployment that was active on the device when the upload was produced.
    """

    destination: Destination
    """Destination-side details of where an upload was written."""

    device_id: str
    """ID of the device that produced the upload."""

    digest: str
    """
    The SHA-256 digest of the uploaded file, formatted as `sha256:` followed by 64
    lowercase hex characters.
    """

    file_rule_id: str
    """ID of the file rule that produced the upload."""

    object: Literal["upload"]
    """The object type, which is always `upload`."""

    release_id: str
    """ID of the release the device was on when the upload was produced."""

    size: int
    """The size of the uploaded file in bytes."""

    source: Source
    """Source-side details of the file on the device that produced an upload."""

    status: UploadStatus
    """The lifecycle status of an upload in the ledger.

    - `pending`: a presigned URL has been minted but the device has not yet
      confirmed a durable write.
    - `uploaded`: the device confirmed a durable write to the bucket.
    """

    updated_at: datetime
    """Timestamp of when the upload was last updated."""

    upload_collection_id: str
    """ID of the upload collection the producing file rule uploads to."""

    upload_collection_name: str
    """The name of the upload collection the producing file rule uploads to."""

    uploaded_at: Optional[datetime] = None
    """Timestamp of when the upload was durably confirmed.

    Null until the upload completes.
    """
