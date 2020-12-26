"""Module for Product Group deletion frame classes (GW_NEW_GROUP)."""
from pyvlx.const import Command, GetGroupInformationStatus

from .frame import FrameBase


class FrameDeleteGroupRequest(FrameBase):
    """Frame for delete product group request."""

    PAYLOAD_LEN = 2

    def __init__(self, group_id=0):
        """Init Frame."""
        super().__init__(Command.GW_DELETE_GROUP_REQ)
        self.group_id = group_id

    def get_payload(self):
        """Return Payload."""
        result = self.group_id.to_bytes(1, "big")
        return result

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.group_id = payload[0]

    def __str__(self):
        """Return human readable string."""
        return '<{} group_id="{}">'.format(
            type(self).__name__, self.group_id
        )


class FrameDeleteGroupNotfication(FrameBase):
    """Frame for delete Group notification."""

    PAYLOAD_LEN = 1

    def __init__(self, group_id=0):
        """Init Frame."""
        super().__init__(Command.GW_GROUP_DELETED_NTF)
        self.group_id = group_id

    def get_payload(self):
        """Return Payload."""
        result = self.group_id.to_bytes(1, "big")
        return result

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.group_id = payload[0]

    def __str__(self):
        """Return human readable string."""
        return '<{} group_id="{}"/>'.format(
            type(self).__name__, self.group_id
        )


class FrameDeleteGroupConfirmation(FrameBase):
    """Frame for delete product group request confirmation."""

    PAYLOAD_LEN = 2

    def __init__(self, group_id=0, status=GetGroupInformationStatus.NO_GROUPS):
        """Init Frame."""
        super().__init__(Command.GW_DELETE_GROUP_CFM)
        self.group_id = group_id
        self.status = status

    def get_payload(self):
        """Return Payload."""
        result = self.status.value.to_bytes(1, "big")
        result += self.group_id.to_bytes(1, "big")
        return result

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.status = GetGroupInformationStatus(payload[0])
        self.group_id = payload[1]

    def __str__(self):
        """Return human readable string."""
        return '<{} status="{}" group_id="{}"/>'.format(
            type(self).__name__, self.status, self.group_id
        )
