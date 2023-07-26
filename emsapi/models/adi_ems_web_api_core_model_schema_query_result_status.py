# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiCoreModelSchemaQueryResultStatus(Model):
    """AdiEmsWebApiCoreModelSchemaQueryResultStatus.

    All required parameters must be populated in order to send to Azure.

    :param message: Required.
    :type message: str
    :param query_status: Required. Possible values include: 'inProgress',
     'success', 'failure', 'undetermined'
    :type query_status: str or ~emsapi.models.enum
    """

    _validation = {
        'message': {'required': True},
        'query_status': {'required': True},
    }

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'query_status': {'key': 'queryStatus', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiCoreModelSchemaQueryResultStatus, self).__init__(**kwargs)
        self.message = kwargs.get('message', None)
        self.query_status = kwargs.get('query_status', None)
