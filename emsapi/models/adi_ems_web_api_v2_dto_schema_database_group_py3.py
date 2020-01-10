# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaDatabaseGroup(Model):
    """Represents a folder in the database tree of an EMS installation.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The unique string identifier for the database group
    :type id: str
    :param name: Required. The display name for the database group
    :type name: str
    :param groups: An ordered listing of child database groups contained in
     this group
    :type groups: list[~emsapi.models.AdiEmsWebApiV2DtoSchemaDatabaseGroup]
    :param databases: An ordered listing of child databases contained in this
     group
    :type databases: list[~emsapi.models.AdiEmsWebApiV2DtoSchemaDatabase]
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'groups': {'key': 'groups', 'type': '[AdiEmsWebApiV2DtoSchemaDatabaseGroup]'},
        'databases': {'key': 'databases', 'type': '[AdiEmsWebApiV2DtoSchemaDatabase]'},
    }

    def __init__(self, *, id: str, name: str, groups=None, databases=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoSchemaDatabaseGroup, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.groups = groups
        self.databases = databases
