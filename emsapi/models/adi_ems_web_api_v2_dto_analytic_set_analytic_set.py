# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAnalyticSetAnalyticSet(Model):
    """Encapsulates the data that defines an AnalyticSet.

    :param name: The name of the AnalyticSet
    :type name: str
    :param description: An optional description of the AnalyticSet.
    :type description: str
    :param items: An array of the analytics contained in the AnalyticSet
    :type items:
     list[~emsapi.models.AdiEmsWebApiV2DtoAnalyticSetAnalyticSetItem]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'items': {'key': 'items', 'type': '[AdiEmsWebApiV2DtoAnalyticSetAnalyticSetItem]'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoAnalyticSetAnalyticSet, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.items = kwargs.get('items', None)
