"""Module for get Group Information frame classes (GW_GET_GROUP_INFORMATION)."""
from pyvlx.const import Command, GetGroupInformationStatus
from pyvlx.dataobjects import DtoProductGroup

from .frame import FrameBase


class FrameGetGroupInformationRequest(FrameBase):
    """Frame for get group information request."""

    PAYLOAD_LEN = 1

    def __init__(self, group_id=0):
        """Init Frame."""
        super().__init__(Command.GW_GET_GROUP_INFORMATION_REQ)
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


class FrameGetGroupInformationConfirmation(FrameBase):
    """Frame for confirmation for get group information request."""

    PAYLOAD_LEN = 2

    def __init__(self, group_id=0, status=GetGroupInformationStatus.NO_GROUPS):
        """Init Frame."""
        super().__init__(Command.GW_GET_GROUP_INFORMATION_CFM)
        self.status = status
        self.group_id = group_id

    def get_payload(self):
        """Return Payload."""
        return bytes([self.group_id])

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.status = GetGroupInformationStatus(payload[0])
        self.group_id = payload[1]

    def __str__(self):
        """Return human readable string."""
        return '<{} status="{}" group_id="{}"/>'.format(
            type(self).__name__, self.status, self.group_id
        )


class FrameGetGroupInformationNotification(FrameBase):
    """Frame for for get group information notification."""

    def __init__(self):
        """Init Frame."""
        super().__init__(Command.GW_GET_GROUP_INFORMATION_NTF)
        self.productgroup = DtoProductGroup()

    def get_payload(self):
        """Return Payload."""
        return self.productgroup.get_payload()

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.productgroup.from_payload(payload)

    def __str__(self):
        """Return human readable string."""
        return '<{0}>{1}<{0}>'.format(
            type(self).__name__, self.productgroup
        )
