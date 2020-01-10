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

    def __init__(self, **kwargs):
        super(AdiEmsWebDataModelEmsSystem, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.dir_adi = kwargs.get('dir_adi', None)
        self.dir_collection = kwargs.get('dir_collection', None)
