# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAnalyticSetUpdateAnalyticSet(Model):
    """Encapsulates the data for updating an existing analytic set.

    :param description: An optional description of the AnalyticSet
    :type description: str
    :param items: An array of the analytics contained in the AnalyticSet
    :type items:
     list[~emsapi.models.AdiEmsWebApiV2DtoAnalyticSetNewAnalyticSetItem]
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'items': {'key': 'items', 'type': '[AdiEmsWebApiV2DtoAnalyticSetNewAnalyticSetItem]'},
    }

    def __init__(self, *, description: str=None, items=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoAnalyticSetUpdateAnalyticSet, self).__init__(**kwargs)
        self.description = description
        self.items = items
