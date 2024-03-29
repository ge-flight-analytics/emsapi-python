# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2ModelAdminApiClientNew(Model):
    """Represents a new API client application that consumes REST services hosted
    in the website that can be provided
    when creating a new client record.

    All required parameters must be populated in order to send to Azure.

    :param client_id: Required. The unique, user friendly, client ID of the
     client used when clients request tokens to access the API
    :type client_id: str
    :param client_secret: The client secret value used when clients request
     tokens to access the API
    :type client_secret: str
    :param grant_type: Required. The grant type that may be used by the client
     to access the API. Possible values include: 'trusted', 'password',
     'implicit'
    :type grant_type: str or ~emsapi.models.enum
    :param description: An optional brief summary describing the API client
     and its purpose
    :type description: str
    :param redirect_uri: The redirect URI for the API client for specific
     grant types (e.g. implicit)
    :type redirect_uri: str
    """

    _validation = {
        'client_id': {'required': True, 'pattern': r'^[^:]*$'},
        'grant_type': {'required': True},
    }

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
        'grant_type': {'key': 'grantType', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'redirect_uri': {'key': 'redirectUri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2ModelAdminApiClientNew, self).__init__(**kwargs)
        self.client_id = kwargs.get('client_id', None)
        self.client_secret = kwargs.get('client_secret', None)
        self.grant_type = kwargs.get('grant_type', None)
        self.description = kwargs.get('description', None)
        self.redirect_uri = kwargs.get('redirect_uri', None)
