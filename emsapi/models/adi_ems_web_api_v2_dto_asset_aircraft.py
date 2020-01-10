# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAssetAircraft(Model):
    """An aircraft in the system refers to an airframe with a particular tail
    number.

    :param id: The identifier of the aircraft within the system
    :type id: int
    :param description: The description for this aircraft
    :type description: str
    :param fleet_ids: Each aircraft can be mapped to 0-N fleets in the system.
     Because a fleet represents a configuration for a airframe and those
     configurations can change over time,
     it stands to reason that each aircraft can be mapped to more than one of
     them
    :type fleet_ids: list[int]
    :param is_active: Whether this aircraft is active in the system
    :type is_active: bool
    :param is_approved: Whether this aircraft has been approved
    :type is_approved: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'fleet_ids': {'key': 'fleetIds', 'type': '[int]'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'is_approved': {'key': 'isApproved', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoAssetAircraft, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.description = kwargs.get('description', None)
        self.fleet_ids = kwargs.get('fleet_ids', None)
        self.is_active = kwargs.get('is_active', None)
        self.is_approved = kwargs.get('is_approved', None)
