# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherTafTafParseOptions(Model):
    """Specifies options to use when calling the TAF parse API.

    All required parameters must be populated in order to send to Azure.

    :param taf: Required. The raw TAF string to parse
    :type taf: str
    :param issue_date: Required. Date information (in ISO 8601 format) the TAF
     was issued, since the TAF format doesn't include this
     information
    :type issue_date: datetime
    """

    _validation = {
        'taf': {'required': True},
        'issue_date': {'required': True},
    }

    _attribute_map = {
        'taf': {'key': 'taf', 'type': 'str'},
        'issue_date': {'key': 'issueDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoWeatherTafTafParseOptions, self).__init__(**kwargs)
        self.taf = kwargs.get('taf', None)
        self.issue_date = kwargs.get('issue_date', None)
