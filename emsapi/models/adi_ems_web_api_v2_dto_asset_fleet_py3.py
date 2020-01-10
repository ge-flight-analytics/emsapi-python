# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAssetFleet(Model):
    """Represents a 'Fleet' in the EMS system.
    A fleet in this sense is a group of aircraft using the same configuration.
    There may be several fleets representing a particular model of aircraft,
    each showing a specific configuration
    of the airframe.

    :param id: The identifier of the fleet within the system.
    :type id: int
    :param description: The description for this fleet.
    :type description: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, description: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoAssetFleet, self).__init__(**kwargs)
        self.id = id
        self.description = description
