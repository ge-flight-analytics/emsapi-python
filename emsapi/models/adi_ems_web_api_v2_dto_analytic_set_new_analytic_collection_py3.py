# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAnalyticSetNewAnalyticCollection(Model):
    """Encapsulates the data for the creation of a new analytic collection.

    :param name: The name of the AnalyticCollection
    :type name: str
    :param description: An optional description of the AnalyticCollection
    :type description: str
    :param items: An array of the analytics contained in the
     AnalyticCollection
    :type items:
     list[~emsapi.models.AdiEmsWebApiV2DtoAnalyticSetNewAnalyticCollectionItem]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'items': {'key': 'items', 'type': '[AdiEmsWebApiV2DtoAnalyticSetNewAnalyticCollectionItem]'},
    }

    def __init__(self, *, name: str=None, description: str=None, items=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoAnalyticSetNewAnalyticCollection, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.items = items
