# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAnalyticSetAnalyticSetGroup(Model):
    """A container for analytic sets.

    :param name: The name of the group
    :type name: str
    :param group_id: The ID of the group. This should be a relative path with
     backslashes replaced with colons
    :type group_id: str
    :param groups: An array of groups contained by this group
    :type groups:
     list[~emsapi.models.AdiEmsWebApiV2DtoAnalyticSetAnalyticSetGroup]
    :param sets: An array of analytic sets contained by this group
    :type sets: list[~emsapi.models.AdiEmsWebApiV2DtoAnalyticSetAnalyticSet]
    :param collections: An array of analytic collections contained by this
     group
    :type collections:
     list[~emsapi.models.AdiEmsWebApiV2DtoAnalyticSetAnalyticCollection]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'groups': {'key': 'groups', 'type': '[AdiEmsWebApiV2DtoAnalyticSetAnalyticSetGroup]'},
        'sets': {'key': 'sets', 'type': '[AdiEmsWebApiV2DtoAnalyticSetAnalyticSet]'},
        'collections': {'key': 'collections', 'type': '[AdiEmsWebApiV2DtoAnalyticSetAnalyticCollection]'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoAnalyticSetAnalyticSetGroup, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.group_id = kwargs.get('group_id', None)
        self.groups = kwargs.get('groups', None)
        self.sets = kwargs.get('sets', None)
        self.collections = kwargs.get('collections', None)
