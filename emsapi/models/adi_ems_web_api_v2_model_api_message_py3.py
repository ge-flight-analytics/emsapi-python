# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2ModelApiMessage(Model):
    """Represents a message used to provide information to users about an action
    that took place in an API request.

    :param type: A categorization of the message. Possible values include:
     'warning', 'error', 'success'
    :type type: str or ~emsapi.models.enum
    :param message: A string message describing an event that occurred in an
     API action or event.
    :type message: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, type=None, message: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2ModelApiMessage, self).__init__(**kwargs)
        self.type = type
        self.message = message
