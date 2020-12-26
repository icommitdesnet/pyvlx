"""Module for Product Group Creation frame classes (GW_NEW_GROUP)."""
from pyvlx.const import Command, AlterGroupStatus
from pyvlx.dataobjects import DtoProductGroup

from .frame import FrameBase


class FrameNewGroupRequest(FrameBase):
    """Frame for new product group request."""

    PAYLOAD_LEN = 96

    def __init__(self, productgroup=None):
        """Init Frame."""
        super().__init__(Command.GW_NEW_GROUP_REQ)
        if isinstance(productgroup, DtoProductGroup):
            self.productgroup = productgroup
        else:
            self.productgroup = DtoProductGroup()

    def get_payload(self):
        """Return Payload."""
        result = self.productgroup.get_payload()[:96]
        return result

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.productgroup.from_payload(payload+0x00.to_bytes(2, "big"))

    def __str__(self):
        """Return human readable string."""
        return '<{0}>{1}<{0}>'.format(
            type(self).__name__, self.productgroup
        )


class FrameNewGroupConfirmation(FrameBase):
    """Frame for confirmation for new group request."""

    PAYLOAD_LEN = 2

    def __init__(self, group_id=0, status=AlterGroupStatus.INVALID):
        """Init Frame."""
        super().__init__(Command.GW_NEW_GROUP_CFM)
        self.group_id = group_id
        self.status = status

    def get_payload(self):
        """Return Payload."""
        result = self.status.value.to_bytes(1, "big")
        result += self.group_id.to_bytes(1, "big")
        return result

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.status = AlterGroupStatus(payload[0])
        self.group_id = payload[1]

    def __str__(self):
        """Return human readable string."""
        return '<{} status="{}" group_id="{}"/>'.format(
            type(self).__name__, self.status, self.group_id
        )
