# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherTafPrediction(Model):
    """Represents a forecast prediction originally included in a TAF.

    All required parameters must be populated in order to send to Azure.

    :param id: The ID used to uniquely identify this prediction on an EMS
     system
    :type id: int
    :param unparsed: Required. The original, unparsed prediction string
    :type unparsed: str
    :param time_from: The predicted start time for the weather in this
     prediction
    :type time_from: datetime
    :param time_to: The predicted end time for the weather in this prediction.
     This is defined by the following predictions start time
     or if it's the last prediction in a TAF it is the end of the validity
     window
    :type time_to: datetime
    :param time_becoming: The time that the prediction weather is expected to
     occur. This is only used with the "Becoming" change
     indicator
    :type time_becoming: datetime
    :param weather_change: Required. The type of conditions change indicator
     specified. When weather conditions are reported as changing this
     is "None". Possible values include: 'none', 'from', 'becoming',
     'temporary', 'probability', 'intermediate'
    :type weather_change: str or ~emsapi.models.enum
    :param probability: The probability of the weather described in this
     prediction occurring
    :type probability: int
    :param wind_direction: The wind direction in degrees or, if wind is
     variable this will be zero
    :type wind_direction: int
    :param wind_speed: The wind speed in knots
    :type wind_speed: int
    :param wind_gust_speed: The wind gust speed in knots, if wind gust data is
     present
    :type wind_gust_speed: int
    :param wind_shear_height: The wind shear height in feet, if wind shear
     data is present
    :type wind_shear_height: int
    :param wind_shear_direction: The wind shear direction in degrees, if wind
     shear data is present
    :type wind_shear_direction: int
    :param wind_shear_speed: The wind shear speed in knots, if wind shear data
     is present
    :type wind_shear_speed: int
    :param visibility_horizontal: The horizontal visibility in statute miles.
     Uses "Infinity" to indicate there is no limit
    :type visibility_horizontal: float
    :param visibility_vertical: The vertical visibility in feet above ground
     level
    :type visibility_vertical: int
    :param pressure: Pressure above ground level in inches of mercury
    :type pressure: float
    :param portion_not_decoded: Any parts of the raw prediction string that
     were unable to be decoded
    :type portion_not_decoded: str
    :param ceiling: The lowest altitude of "Broken" or "Overcast" cloud
     conditions or vertical visibility. Uses "Infinity" to
     indicate there is no limit
    :type ceiling: float
    :param cloud_conditions: A list of cloud conditions occurring during the
     prediction
    :type cloud_conditions:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherCloudCondition]
    :param icing_conditions: A list of icing conditions occurring during the
     prediction
    :type icing_conditions:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherTafIcingCondition]
    :param turbulence_conditions: A list of turbulence conditions occurring
     during the prediction
    :type turbulence_conditions:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherTafTurbulenceCondition]
    :param temperatures: A list of temperature conditions occurring during the
     prediction
    :type temperatures:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherTafTemperature]
    """

    _validation = {
        'unparsed': {'required': True},
        'weather_change': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'unparsed': {'key': 'unparsed', 'type': 'str'},
        'time_from': {'key': 'timeFrom', 'type': 'iso-8601'},
        'time_to': {'key': 'timeTo', 'type': 'iso-8601'},
        'time_becoming': {'key': 'timeBecoming', 'type': 'iso-8601'},
        'weather_change': {'key': 'weatherChange', 'type': 'str'},
        'probability': {'key': 'probability', 'type': 'int'},
        'wind_direction': {'key': 'windDirection', 'type': 'int'},
        'wind_speed': {'key': 'windSpeed', 'type': 'int'},
        'wind_gust_speed': {'key': 'windGustSpeed', 'type': 'int'},
        'wind_shear_height': {'key': 'windShearHeight', 'type': 'int'},
        'wind_shear_direction': {'key': 'windShearDirection', 'type': 'int'},
        'wind_shear_speed': {'key': 'windShearSpeed', 'type': 'int'},
        'visibility_horizontal': {'key': 'visibilityHorizontal', 'type': 'float'},
        'visibility_vertical': {'key': 'visibilityVertical', 'type': 'int'},
        'pressure': {'key': 'pressure', 'type': 'float'},
        'portion_not_decoded': {'key': 'portionNotDecoded', 'type': 'str'},
        'ceiling': {'key': 'ceiling', 'type': 'float'},
        'cloud_conditions': {'key': 'cloudConditions', 'type': '[AdiEmsWebApiV2DtoWeatherCloudCondition]'},
        'icing_conditions': {'key': 'icingConditions', 'type': '[AdiEmsWebApiV2DtoWeatherTafIcingCondition]'},
        'turbulence_conditions': {'key': 'turbulenceConditions', 'type': '[AdiEmsWebApiV2DtoWeatherTafTurbulenceCondition]'},
        'temperatures': {'key': 'temperatures', 'type': '[AdiEmsWebApiV2DtoWeatherTafTemperature]'},
    }

    def __init__(self, *, unparsed: str, weather_change, id: int=None, time_from=None, time_to=None, time_becoming=None, probability: int=None, wind_direction: int=None, wind_speed: int=None, wind_gust_speed: int=None, wind_shear_height: int=None, wind_shear_direction: int=None, wind_shear_speed: int=None, visibility_horizontal: float=None, visibility_vertical: int=None, pressure: float=None, portion_not_decoded: str=None, ceiling: float=None, cloud_conditions=None, icing_conditions=None, turbulence_conditions=None, temperatures=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoWeatherTafPrediction, self).__init__(**kwargs)
        self.id = id
        self.unparsed = unparsed
        self.time_from = time_from
        self.time_to = time_to
        self.time_becoming = time_becoming
        self.weather_change = weather_change
        self.probability = probability
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed
        self.wind_gust_speed = wind_gust_speed
        self.wind_shear_height = wind_shear_height
        self.wind_shear_direction = wind_shear_direction
        self.wind_shear_speed = wind_shear_speed
        self.visibility_horizontal = visibility_horizontal
        self.visibility_vertical = visibility_vertical
        self.pressure = pressure
        self.portion_not_decoded = portion_not_decoded
        self.ceiling = ceiling
        self.cloud_conditions = cloud_conditions
        self.icing_conditions = icing_conditions
        self.turbulence_conditions = turbulence_conditions
        self.temperatures = temperatures
