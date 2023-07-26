# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAnalyticSetAnalyticSetGroupCreated(Model):
    """The result of a newly created group.

    :param group_id: The group identifier for the newly created group
    :type group_id: str
    :param location: The URI location for the newly created group
    :type location: str
    """

    _attribute_map = {
        'group_id': {'key': 'groupId', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, group_id: str=None, location: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoAnalyticSetAnalyticSetGroupCreated, self).__init__(**kwargs)
        self.group_id = group_id
        self.location = location