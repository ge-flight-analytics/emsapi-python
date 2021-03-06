# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebDataModelEmsSystem(Model):
    """AdiEmsWebDataModelEmsSystem.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param description:
    :type description: str
    :param dir_adi:
    :type dir_adi: str
    :param dir_collection:
    :type dir_collection: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'dir_adi': {'key': 'dirAdi', 'type': 'str'},
        'dir_collection': {'key': 'dirCollection', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, name: str=None, description: str=None, dir_adi: str=None, dir_collection: str=None, **kwargs) -> None:
        super(AdiEmsWebDataModelEmsSystem, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.description = description
        self.dir_adi = dir_adi
        self.dir_collection = dir_collection
