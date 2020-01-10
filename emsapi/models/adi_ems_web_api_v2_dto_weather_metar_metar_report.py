# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherMetarMetarReport(Model):
    """Represents an individual METAR report.

    All required parameters must be populated in order to send to Azure.

    :param unparsed: Required. The unparsed but de-identified METAR string
    :type unparsed: str
    :param airport: Required. The airport that issued the METAR report
    :type airport: str
    :param issued: The day, hour and minute the METAR was issued. May also
     optionally contain the month and year issued if the
     date contextual information is available
    :type issued: datetime
    :param is_automatic: Required. Indicates whether the original METAR data
     was automatically generated
    :type is_automatic: bool
    :param wind_direction: The wind direction in degrees or, if wind is
     variable this will be zero
    :type wind_direction: float
    :param wind_speed: The wind speed in knots
    :type wind_speed: float
    :param wind_gust_speed: The wind gust speed in knots, if wind gust data is
     present
    :type wind_gust_speed: float
    :param wind_direction_variable_start: When wind is variable, the
     approximate end range of the wind direction in degrees
    :type wind_direction_variable_start: float
    :param wind_direction_variable_end: When wind is variable, the approximate
     end range of the wind direction in degrees
    :type wind_direction_variable_end: float
    :param effective_visibility: The effective visibility in statute miles
    :type effective_visibility: float
    :param exact_visibility: The exact reported visibility in statute miles.
     Uses "Infinity" to indicate there is no limit
    :type exact_visibility: float
    :param visibility_qualifier: A qualifier describing the current exact
     reported visibility. Possible values include: 'equal', 'greaterThan',
     'lessThan'
    :type visibility_qualifier: str or ~emsapi.models.enum
    :param runway_visual_ranges: A list of runway visual ranges for reported
     runways
    :type runway_visual_ranges:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherMetarRunwayVisualRange]
    :param current_weather: A list of current weather phenomenons
    :type current_weather:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherWeatherPhenomenon]
    :param recent_weather: A list of recently occurring weather phenomenons
    :type recent_weather:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherWeatherPhenomenon]
    :param is_weather_data_valid: Required. Indicates whether all
     current/recent reported weather phenomenons had valid sensor data
    :type is_weather_data_valid: bool
    :param cloud_conditions: A list of current cloud conditions
    :type cloud_conditions:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherCloudCondition]
    :param ceiling: The lowest "Broken", "Overcast" or "Vertical Visibility"
     cloud conditions associated with this object
    :type ceiling: ~emsapi.models.AdiEmsWebApiV2DtoWeatherCloudCondition
    :param is_cloud_data_valid: Required. Indicates whether all reported cloud
     conditions had valid sensor data
    :type is_cloud_data_valid: bool
    :param max_cloud_height: The maximum height of the base of a visual
     portion of one of the cloud conditions associated with this
     object. Uses "Infinity" to indicate there is no limit
    :type max_cloud_height: float
    :param temperature: The current temperature value in degrees Celsius
    :type temperature: float
    :param dewpoint: The current dew point value in degrees Celsius
    :type dewpoint: float
    :param pressure: Pressure above ground level in inches of mercury
    :type pressure: float
    :param runway_conditions: A list of current runway conditions
    :type runway_conditions:
     list[~emsapi.models.AdiEmsWebApiV2DtoWeatherMetarRunwayCondition]
    :param flight_match_type: The time and place relative to a specific flight
     that this METAR data would match to. Possible values include: 'none',
     'takeoff', 'landing'
    :type flight_match_type: str or ~emsapi.models.enum
    """

    _validation = {
        'unparsed': {'required': True},
        'airport': {'required': True},
        'is_automatic': {'required': True},
        'is_weather_data_valid': {'required': True},
        'is_cloud_data_valid': {'required': True},
    }

    _attribute_map = {
        'unparsed': {'key': 'unparsed', 'type': 'str'},
        'airport': {'key': 'airport', 'type': 'str'},
        'issued': {'key': 'issued', 'type': 'iso-8601'},
        'is_automatic': {'key': 'isAutomatic', 'type': 'bool'},
        'wind_direction': {'key': 'windDirection', 'type': 'float'},
        'wind_speed': {'key': 'windSpeed', 'type': 'float'},
        'wind_gust_speed': {'key': 'windGustSpeed', 'type': 'float'},
        'wind_direction_variable_start': {'key': 'windDirectionVariableStart', 'type': 'float'},
        'wind_direction_variable_end': {'key': 'windDirectionVariableEnd', 'type': 'float'},
        'effective_visibility': {'key': 'effectiveVisibility', 'type': 'float'},
        'exact_visibility': {'key': 'exactVisibility', 'type': 'float'},
        'visibility_qualifier': {'key': 'visibilityQualifier', 'type': 'str'},
        'runway_visual_ranges': {'key': 'runwayVisualRanges', 'type': '[AdiEmsWebApiV2DtoWeatherMetarRunwayVisualRange]'},
        'current_weather': {'key': 'currentWeather', 'type': '[AdiEmsWebApiV2DtoWeatherWeatherPhenomenon]'},
        'recent_weather': {'key': 'recentWeather', 'type': '[AdiEmsWebApiV2DtoWeatherWeatherPhenomenon]'},
        'is_weather_data_valid': {'key': 'isWeatherDataValid', 'type': 'bool'},
        'cloud_conditions': {'key': 'cloudConditions', 'type': '[AdiEmsWebApiV2DtoWeatherCloudCondition]'},
        'ceiling': {'key': 'ceiling', 'type': 'AdiEmsWebApiV2DtoWeatherCloudCondition'},
        'is_cloud_data_valid': {'key': 'isCloudDataValid', 'type': 'bool'},
        'max_cloud_height': {'key': 'maxCloudHeight', 'type': 'float'},
        'temperature': {'key': 'temperature', 'type': 'float'},
        'dewpoint': {'key': 'dewpoint', 'type': 'float'},
        'pressure': {'key': 'pressure', 'type': 'float'},
        'runway_conditions': {'key': 'runwayConditions', 'type': '[AdiEmsWebApiV2DtoWeatherMetarRunwayCondition]'},
        'flight_match_type': {'key': 'flightMatchType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoWeatherMetarMetarReport, self).__init__(**kwargs)
        self.unparsed = kwargs.get('unparsed', None)
        self.airport = kwargs.get('airport', None)
        self.issued = kwargs.get('issued', None)
        self.is_automatic = kwargs.get('is_automatic', None)
        self.wind_direction = kwargs.get('wind_direction', None)
        self.wind_speed = kwargs.get('wind_speed', None)
        self.wind_gust_speed = kwargs.get('wind_gust_speed', None)
        self.wind_direction_variable_start = kwargs.get('wind_direction_variable_start', None)
        self.wind_direction_variable_end = kwargs.get('wind_direction_variable_end', None)
        self.effective_visibility = kwargs.get('effective_visibility', None)
        self.exact_visibility = kwargs.get('exact_visibility', None)
        self.visibility_qualifier = kwargs.get('visibility_qualifier', None)
        self.runway_visual_ranges = kwargs.get('runway_visual_ranges', None)
        self.current_weather = kwargs.get('current_weather', None)
        self.recent_weather = kwargs.get('recent_weather', None)
        self.is_weather_data_valid = kwargs.get('is_weather_data_valid', None)
        self.cloud_conditions = kwargs.get('cloud_conditions', None)
        self.ceiling = kwargs.get('ceiling', None)
        self.is_cloud_data_valid = kwargs.get('is_cloud_data_valid', None)
        self.max_cloud_height = kwargs.get('max_cloud_height', None)
        self.temperature = kwargs.get('temperature', None)
        self.dewpoint = kwargs.get('dewpoint', None)
        self.pressure = kwargs.get('pressure', None)
        self.runway_conditions = kwargs.get('runway_conditions', None)
        self.flight_match_type = kwargs.get('flight_match_type', None)
