# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2ModelTableauTrusted(Model):
    """Represents information that can be used to access Tableau content related
    to an associated Tableau server.

    :param trusted_url: The URL that can be used to start a trusted session
     with the Tableau server.
    :type trusted_url: str
    :param url: The root URL of the Tableau server with site.
    :type url: str
    :param site: The site that the TrustedUrl is able to access when used.
    :type site: str
    """

    _attribute_map = {
        'trusted_url': {'key': 'trustedUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'site': {'key': 'site', 'type': 'str'},
    }

    def __init__(self, *, trusted_url: str=None, url: str=None, site: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2ModelTableauTrusted, self).__init__(**kwargs)
        self.trusted_url = trusted_url
        self.url = url
        self.site = site
