"""Module for Dataobjects."""
from datetime import datetime
import time
from pyvlx.const import GroupType, Velocity, NodeVariation
from pyvlx.exception import PyVLXException
from pyvlx.helpers import (bytes_to_string, string_to_bytes,
                           bytes_from_statusflags, statusflags_from_bytes)


class DtoLocalTime:
    """Dataobject to hold KLF200 Time Data."""

    def __init__(self, utctime=None, localtime=None):
        """Initialize DtoLocalTime class."""
        if utctime is None:
            utctime = datetime.fromtimestamp(0)
        if localtime is None:
            localtime = datetime.fromtimestamp(0)
        self.utctime = utctime
        self.localtime = localtime

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} utctime="{}" localtime="{}"/>'.format(
                type(self).__name__, self.utctime, self.localtime)
        )

    def from_payload(self, payload):
        """Build the Dto From Data."""
        self.utctime = datetime.fromtimestamp(int.from_bytes(payload[0:4], "big"))
        weekday = payload[11] - 1
        if weekday == -1:
            weekday = 6

        self.localtime = datetime.fromtimestamp(time.mktime(
            (int.from_bytes(payload[9:11], "big") + 1900,  # Year
             payload[8],  # month
             payload[7],  # day
             payload[6],  # hour
             payload[5],  # minute
             payload[4],  # second
             weekday,
             int.from_bytes(payload[12:14], "big"),  # day of year
             int.from_bytes(payload[14:15], byteorder='big', signed=True))))

    def to_payload(self):
        """Build the Dto From Data."""
        payload = b''
        payload = int(self.utctime.timestamp()).to_bytes(4, "big")
        payload += self.localtime.second.to_bytes(1, "big")
        payload += self.localtime.minute.to_bytes(1, "big")
        payload += self.localtime.hour.to_bytes(1, "big")
        payload += self.localtime.day.to_bytes(1, "big")
        payload += self.localtime.month.to_bytes(1, "big")
        payload += (self.localtime.year - 1900).to_bytes(2, "big")
        if self.localtime.weekday == 6:
            payload += (0).to_bytes(1, "big")
        else:
            payload += (self.localtime.weekday() + 1).to_bytes(1, "big")
        payload += self.localtime.timetuple().tm_yday.to_bytes(2, "big")
        payload += (self.localtime.timetuple().tm_isdst).to_bytes(1, "big", signed=True)
        return payload


class DtoNetworkSetup:
    """Dataobject to hold KLF200 Network Setup."""

    def __init__(self, ipaddress=None, gateway=None, netmask=None, dhcp=None):
        """Initialize DtoNetworkSetup class."""
        self.ipaddress = ipaddress
        self.gateway = gateway
        self.netmask = netmask
        self.dhcp = dhcp

    def __str__(self):
        """Return human readable string."""
        return '<{} ipaddress="{}" gateway="{}" gateway="{}"  dhcp="{}"/>'.format(
            type(self).__name__, self.ipaddress, self.gateway,
            self.gateway, self.dhcp
        )


class DtoProtocolVersion:
    """KLF 200 Dataobject for Protocol version."""

    def __init__(self, majorversion=None, minorversion=None):
        """Initialize DtoProtocolVersion class."""
        self.majorversion = majorversion
        self.minorversion = minorversion

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} majorversion="{}" minorversion="{}"/>'.format(
                type(self).__name__, self.majorversion, self.minorversion
            )
        )


class DtoState:
    """Data Object for Gateway State."""

    def __init__(self, gateway_state=None, gateway_sub_state=None):
        """Initialize DtoState class."""
        self.gateway_state = gateway_state
        self.gateway_sub_state = gateway_sub_state

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} gateway_state="{}" gateway_sub_state="{}"/>'.format(
                type(self).__name__, self.gateway_state, self.gateway_sub_state
            )
        )


class DtoVersion:
    """Object for KLF200 Version Information."""

    def __init__(self,
                 softwareversion=None, hardwareversion=None, productgroup=None, producttype=None):
        """Initialize DtoVersion class."""
        self.softwareversion = softwareversion
        self.hardwareversion = hardwareversion
        self.productgroup = productgroup
        self.producttype = producttype

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} softwareversion="{}" hardwareversion="{}" '
            'productgroup="{}" producttype="{}"/>'.format(
                type(self).__name__,
                self.softwareversion, self.hardwareversion, self.productgroup, self.producttype
            )
        )


class DtoLeaveLearnState:
    """Dataobject to hold KLF200 Data."""

    def __init__(self, status=None):
        """Initialize DtoLeaveLearnState class."""
        self.status = status

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} status="{}"/>'.format(
                type(self).__name__, self.status
            )
        )


class DtoProductGroup:
    """Object for Product Group Information."""

    def __init__(self,
                 group_id=0,
                 order=0,
                 placement=0,
                 name='',
                 velocity=Velocity.NOT_AVAILABLE,
                 nodevariation=NodeVariation.NOT_SET,
                 grouptype=GroupType.ALL_GROUP,
                 numberofobjects=0,
                 node_ids=None,
                 revision=0
                 ):
        """Initialize DtoVersion class."""
        self.group_id = group_id
        self.order = order
        self.placement = placement
        self.name = name
        self.velocity = velocity
        self.nodevariation = nodevariation
        self.grouptype = grouptype
        self.numberofobjects = numberofobjects
        self.node_ids = node_ids
        self.revision = revision

    def from_payload(self, payload):
        """Init Data Object from binary data."""
        self.group_id = payload[0]
        self.order = payload[1] * 256 + payload[2]
        self.placement = payload[3]
        self.name = bytes_to_string(payload[4:68])
        self.velocity = Velocity(payload[68])
        self.nodevariation = NodeVariation(payload[69])
        self.grouptype = GroupType(payload[70])
        if self.grouptype == GroupType.USER_GROUP:
            self.numberofobjects = payload[71]
            self.node_ids = statusflags_from_bytes(payload[72:97])
            if len(self.node_ids) != self.numberofobjects:
                raise PyVLXException("product_group_information_incomplete")
        else:
            self.numberofobjects = 0
            self.node_ids = []
        self.revision = payload[97] * 256 + payload[98]

    def get_payload(self):
        """Return Payload."""
        payload = self.group_id.to_bytes(1, "big")
        payload += self.order.to_bytes(2, "big")
        payload += self.placement.to_bytes(1, "big")
        payload += string_to_bytes(self.name, 64)
        payload += self.velocity.value.to_bytes(1, "big")
        payload += self.nodevariation.value.to_bytes(1, "big")
        payload += self.grouptype.value.to_bytes(1, "big")
        payload += len(self.node_ids).to_bytes(1, "big")
        payload += bytes_from_statusflags(self.node_ids, 25)
        payload += self.revision.to_bytes(2, "big")
        return payload

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} group_id="{}" order="{}" placement="{}" '
            'name="{}" velocity="{}" nodevariation="{}" '
            'grouptype="{}" node_ids="{}" producttype="{}"/>'.format(
                type(self).__name__,
                self.group_id, self.order, self.placement,
                self.name, self.velocity, self.nodevariation,
                self.grouptype, self.node_ids, self.revision
            )
        )
