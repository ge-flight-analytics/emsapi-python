# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2ModelAdminGroup(Model):
    """Represents a group that is used to control security for website users that
    are members of the group.

    All required parameters must be populated in order to send to Azure.

    :param id: The unique integer identifier of the group.
    :type id: int
    :param name: Required. The unique, user friendly, name of the group.
    :type name: str
    :param description: A brief summary describing the group and its members
     and purpose.
    :type description: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, name: str, id: int=None, description: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2ModelAdminGroup, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.description = description