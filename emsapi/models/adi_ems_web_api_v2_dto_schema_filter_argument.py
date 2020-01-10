# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaFilterArgument(Model):
    """Represents an argument in a filter.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The type of the filter argument, describing the
     role of the argument. Possible values include: 'none', 'filter', 'field',
     'constant'
    :type type: str or ~emsapi.models.enum
    :param value: Required. The value represented by the filter argument.
    :type value: object
    """

    _validation = {
        'type': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoSchemaFilterArgument, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.value = kwargs.get('value', None)
