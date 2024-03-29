# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaFieldInfo(Model):
    """Represents the result of a query to retrieve info for multiple fields.

    All required parameters must be populated in order to send to Azure.

    :param fields: Required. Information about the available fields that were
     requested in the query
    :type fields: list[~emsapi.models.AdiEmsWebApiV2DtoSchemaField]
    :param invalid_field_ids: The ids for fields that were requested in the
     query but are unavailable.
    :type invalid_field_ids: list[str]
    """

    _validation = {
        'fields': {'required': True},
    }

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '[AdiEmsWebApiV2DtoSchemaField]'},
        'invalid_field_ids': {'key': 'invalidFieldIds', 'type': '[str]'},
    }

    def __init__(self, *, fields, invalid_field_ids=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoSchemaFieldInfo, self).__init__(**kwargs)
        self.fields = fields
        self.invalid_field_ids = invalid_field_ids
