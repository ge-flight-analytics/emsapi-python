# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaQueryTracking(Model):
    """Additional options that may be provided as part of a data source query to
    enable querying for only new or updated data.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. A unique name for the tracked query to be used
     across multiple API calls. This must be a globally
     unique string that should not conflict with other tracked queries
    :type name: str
    :param batch_id: An optional unique id (guid) to associate with this
     particular instance of the tracked query. If this
     is not specified a new batch id will be automatically generated by the
     API. The batch id is returned
     as part of the query results and may be used to roll back individual
     queries
    :type batch_id: str
    :param mode: An optional mode that specifies which types of records should
     be returned as part of the tracked query.
     The omission of this property results in the query returning only new
     records since the last time the
     tracked query was performed. Possible values include: 'all', 'onlyNew'
    :type mode: str or ~emsapi.models.enum
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'batch_id': {'key': 'batchId', 'type': 'str'},
        'mode': {'key': 'mode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoSchemaQueryTracking, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.batch_id = kwargs.get('batch_id', None)
        self.mode = kwargs.get('mode', None)
