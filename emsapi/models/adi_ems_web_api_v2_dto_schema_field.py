# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaField(Model):
    """Represents an individual field that can be accessed within a data source.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The unique string identifier for the field
    :type id: str
    :param type: Required. The data type of the underlying data stored for the
     field. Possible values include: 'boolean', 'dateTime', 'discrete',
     'number', 'string'
    :type type: str or ~emsapi.models.enum
    :param name: Required. The display name for the field
    :type name: str
    :param path: An ordered list of groupIds that make up the path to this
     field, excluding the root group.
     The last groupId is the parent group of this field
    :type path: list[str]
    :param display_path: An ordered list of group names that make up the path
     to this field, excluding the root group.
     The last entry is the parent group of this field
    :type display_path: list[str]
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': '[str]'},
        'display_path': {'key': 'displayPath', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoSchemaField, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.type = kwargs.get('type', None)
        self.name = kwargs.get('name', None)
        self.path = kwargs.get('path', None)
        self.display_path = kwargs.get('display_path', None)
