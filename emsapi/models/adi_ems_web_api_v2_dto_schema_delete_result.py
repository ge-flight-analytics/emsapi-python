# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaDeleteResult(Model):
    """Represents the result of an update.

    All required parameters must be populated in order to send to Azure.

    :param rows_deleted: Required. The number of rows deleted
    :type rows_deleted: int
    """

    _validation = {
        'rows_deleted': {'required': True},
    }

    _attribute_map = {
        'rows_deleted': {'key': 'rowsDeleted', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoSchemaDeleteResult, self).__init__(**kwargs)
        self.rows_deleted = kwargs.get('rows_deleted', None)
