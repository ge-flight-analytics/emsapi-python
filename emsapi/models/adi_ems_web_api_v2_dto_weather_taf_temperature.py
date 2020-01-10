# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherTafTemperature(Model):
    """Describes a forecast temperature.

    :param valid_time: Describes the time at which the temperature forecast is
     valid
    :type valid_time: datetime
    :param surface: The expected surface temperature value
    :type surface: float
    :param maximum: The expected maximum temperature value
    :type maximum: float
    :param minimum: The expected minimum temperature value
    :type minimum: float
    """

    _attribute_map = {
        'valid_time': {'key': 'validTime', 'type': 'iso-8601'},
        'surface': {'key': 'surface', 'type': 'float'},
        'maximum': {'key': 'maximum', 'type': 'float'},
        'minimum': {'key': 'minimum', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoWeatherTafTemperature, self).__init__(**kwargs)
        self.valid_time = kwargs.get('valid_time', None)
        self.surface = kwargs.get('surface', None)
        self.maximum = kwargs.get('maximum', None)
        self.minimum = kwargs.get('minimum', None)
