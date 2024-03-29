# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoExportServiceServiceInfo(Model):
    """Represents information about an export service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The unique identifier of the service
    :type id: str
    :param name: Required. The (display) name of the service
    :type name: str
    :ivar type: Required. The type of export service. Default value:
     "analytic" .
    :vartype type: str
    :param database_id: Required. The database identifier associated with this
     export
    :type database_id: str
    :param enabled: Required. Whether the service is currently enabled
    :type enabled: bool
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
        'database_id': {'required': True},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'database_id': {'key': 'databaseId', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    type = "analytic"

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoExportServiceServiceInfo, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.database_id = kwargs.get('database_id', None)
        self.enabled = kwargs.get('enabled', None)
