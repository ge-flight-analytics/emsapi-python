# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaQueryResultHeader(Model):
    """Represents a header column in data source query result.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The unique string identifier of the field associated
     with this column
    :type id: str
    :param name: Required. The user-friendly display name of the field
     associated with this column
    :type name: str
    :param format: Required. The format applied to the values for the field
     associated with this column. Possible values include: 'none', 'display'
    :type format: str or ~emsapi.models.enum
    :param units: The units of values of the field associated with this
     column. This value may be empty if not applicable
    :type units: str
    :param aggregate: The aggregate operation performed on this column. This
     value may be empty if not applicable. Possible values include: 'none',
     'avg', 'count', 'max', 'min', 'stdev', 'sum', 'var'
    :type aggregate: str or ~emsapi.models.enum
    :param original_id: The unique string identifier of the field associated
     with this column as defined in the original request.
     This is only set when the query is altered due to the fieldId used in
     order to match the database queried against
    :type original_id: str
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
        'format': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'format': {'key': 'format', 'type': 'str'},
        'units': {'key': 'units', 'type': 'str'},
        'aggregate': {'key': 'aggregate', 'type': 'str'},
        'original_id': {'key': 'originalId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoSchemaQueryResultHeader, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.format = kwargs.get('format', None)
        self.units = kwargs.get('units', None)
        self.aggregate = kwargs.get('aggregate', None)
        self.original_id = kwargs.get('original_id', None)
