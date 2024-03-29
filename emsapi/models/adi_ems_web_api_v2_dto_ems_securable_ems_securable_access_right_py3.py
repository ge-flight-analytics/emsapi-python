# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoEmsSecurableEmsSecurableAccessRight(Model):
    """An access right that can be applied to a securable.

    :param name: The name of the access right
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoEmsSecurableEmsSecurableAccessRight, self).__init__(**kwargs)
        self.name = name
