# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherMetarMetarParseOptions(Model):
    """Specifies options to use when calling the METAR parse API.

    All required parameters must be populated in order to send to Azure.

    :param metar: Required. The raw METAR string to parse
    :type metar: str
    :param issue_date: Optional date information (in ISO 8601 format) the
     METAR was issued, since the METAR format only includes
     day, hour and minute time information.
    :type issue_date: datetime
    """

    _validation = {
        'metar': {'required': True},
    }

    _attribute_map = {
        'metar': {'key': 'metar', 'type': 'str'},
        'issue_date': {'key': 'issueDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoWeatherMetarMetarParseOptions, self).__init__(**kwargs)
        self.metar = kwargs.get('metar', None)
        self.issue_date = kwargs.get('issue_date', None)
