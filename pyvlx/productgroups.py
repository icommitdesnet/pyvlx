"""Module for storing productgroups."""
from pyvlx.dataobjects import DtoProductGroup as Productgroup
from pyvlx.const import GroupType
from .api import (GetAllProductGroups, GetProductGroup)
from .exception import PyVLXException


class Productgroups:
    """Object for storing productgroup objects."""

    def __init__(self, pyvlx):
        """Initialize Productgroups object."""
        self.pyvlx = pyvlx
        self.__productgroups = []

    def __iter__(self):
        """Iterate."""
        yield from self.__productgroups

    def __getitem__(self, key):
        """Return Productgroup by name or by index."""
        if isinstance(key, int):
            for productgroup in self.__productgroups:
                if productgroup.group_id == key:
                    return productgroup
        for productgroup in self.__productgroups:
            if productgroup.name == key:
                return productgroup
        raise KeyError

    def __contains__(self, key):
        """Check if key is in index."""
        if isinstance(key, int):
            for productgroup in self.__productgroups:
                if productgroup.group_id == key:
                    return True
        if isinstance(key, Productgroup):
            for productgroup in self.__productgroups:
                if productgroup == key:
                    return True
        for productgroup in self.__productgroups:
            if productgroup.name == key:
                return True
        return False

    def __len__(self):
        """Return number of nodes."""
        return len(self.__productgroups)

    def add(self, productgroup):
        """Add Productgroup, replace existing productgroup.

        If productgroup with group_id is present.
        """
        if not isinstance(productgroup, Productgroup):
            raise TypeError()
        for i, j in enumerate(self.__productgroups):
            if j.group_id == productgroup.group_id:
                self.__productgroups[i] = productgroup
                return
        self.__productgroups.append(productgroup)

    def clear(self):
        """Clear internal productgroups array."""
        self.__productgroups = []

    async def load(self, group_id=None):
        """Load Productgroups from KLF 200, if no group_id is specified all nodes are loaded."""
        if group_id is not None:
            await self._load_group(group_id=group_id)
        else:
            await self._load_all_groups()

    async def _load_group(self, group_id=0):
        """Load single Productgroup via API."""
#        get_node_information = GetNodeInformation(pyvlx=self.pyvlx, node_id=node_id)
#        await get_node_information.do_api_call()
#        if not get_node_information.success:
#            raise PyVLXException("Unable to retrieve node information")
#        notification_frame = get_node_information.notification_frame
#        node = convert_frame_to_node(self.pyvlx, notification_frame)
#        if node is not None:
#            self.add(node)
        get_product_group = GetProductGroup(pyvlx=self.pyvlx, group_id=group_id)
        await get_product_group.do_api_call()
        if not get_product_group.success:
            raise PyVLXException("Unable to retrieve product group information")
        self.add(get_product_group.productgroup)

    async def _load_all_groups(self):
        """Load all nodes via API."""
        get_all_product_groups = GetAllProductGroups(pyvlx=self.pyvlx,
                                                     usefilter=False,
                                                     filtertype=GroupType.USER_GROUP)
        await get_all_product_groups.do_api_call()
        if not get_all_product_groups.success:
            raise PyVLXException("Unable to retrieve product groups information")
        get_all_product_groups = GetAllProductGroups(pyvlx=self.pyvlx,
                                                     usefilter=False,
                                                     filtertype=GroupType.ROOM)
        await get_all_product_groups.do_api_call()
        if not get_all_product_groups.success:
            raise PyVLXException("Unable to retrieve product groups information")
        get_all_product_groups = GetAllProductGroups(pyvlx=self.pyvlx,
                                                     usefilter=False,
                                                     filtertype=GroupType.HOUSE)
        await get_all_product_groups.do_api_call()
        if not get_all_product_groups.success:
            raise PyVLXException("Unable to retrieve product groups information")
        get_all_product_groups = GetAllProductGroups(pyvlx=self.pyvlx,
                                                     usefilter=False,
                                                     filtertype=GroupType.ALL_GROUP)
        await get_all_product_groups.do_api_call()
        if not get_all_product_groups.success:
            raise PyVLXException("Unable to retrieve product groups information")

        self.clear()
        # XXX: todo build group and append
#        for notification_frame in get_all_product_groups.notification_frames:
#            node = convert_frame_to_node(self.pyvlx, notification_frame)
#            if node is not None:
#                self.add(node)
