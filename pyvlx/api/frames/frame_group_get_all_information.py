"""Module for get All Groups Information frame classes (GW_GET_ALL_GROUPS_INFORMATION)."""
from pyvlx.const import Command, GetGroupInformationStatus, GroupType
from pyvlx.dataobjects import DtoProductGroup
from .frame import FrameBase


class FrameGetAllGroupsInformationRequest(FrameBase):
    """Frame for get all groups information request."""

    PAYLOAD_LEN = 2

    def __init__(self, usefilter=False, filtertype=GroupType.ALL_GROUP):
        """Init Frame."""
        super().__init__(Command.GW_GET_ALL_GROUPS_INFORMATION_REQ)
        self.usefilter = usefilter
        self.filtertype = filtertype

    def get_payload(self):
        """Return Payload."""
        result = self.usefilter.to_bytes(1, "big")
        result += self.filtertype.value.to_bytes(1, "big")
        return result

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.usefilter = payload[0]
        self.filtertype = GroupType(payload[1])

    def __str__(self):
        """Return human readable string."""
        return '<{} usefilter="{}" filtertype="{}"/>'.format(
            type(self).__name__, self.usefilter, self.filtertype
        )


class FrameGetAllGroupsInformationConfirmation(FrameBase):
    """Frame for confirmation for get all groups information request."""

    PAYLOAD_LEN = 2

    def __init__(self, count_groups=0, status=GetGroupInformationStatus.NO_GROUPS):
        """Init Frame."""
        super().__init__(Command.GW_GET_ALL_GROUPS_INFORMATION_CFM)
        self.status = status
        self.count_groups = count_groups

    def get_payload(self):
        """Return Payload."""
        return bytes([self.count_groups])

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.status = GetGroupInformationStatus(payload[0])
        self.count_groups = payload[1]

    def __str__(self):
        """Return human readable string."""
        return '<{} status="{}" count_groups="{}"/>'.format(
            type(self).__name__, self.status, self.count_groups
        )


class FrameGetAllGroupsInformationNotification(FrameBase):
    """Frame for for get all groups information notification."""

    def __init__(self):
        """Init Frame."""
        super().__init__(Command.GW_GET_ALL_GROUPS_INFORMATION_NTF)
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


class FrameGetAllGroupsInformationFinishedNotification(FrameBase):
    """Frame for notification of all groups information finished notification."""

    PAYLOAD_LEN = 0

    def __init__(self):
        """Init Frame."""
        super().__init__(Command.GW_GET_ALL_GROUPS_INFORMATION_FINISHED_NTF)
