# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAnalyticGroup(Model):
    """Represents a group in the exposed tree of analytics for an EMS
    installation.

    :param id: The identifier of the group
    :type id: str
    :param name: The name of the group
    :type name: str
    :param description: The description of the group
    :type description: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, description: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoAnalyticGroup, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.description = description
