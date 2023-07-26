# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoNavigationNavigationWaypoint(Model):
    """Various pieces of information associated with a waypoint.

    :param id: The unique identifier of the waypoint
    :type id: int
    :param airport_id: The airport id for the waypoint, if any
    :type airport_id: int
    :param country_code: The country code of the waypoint
    :type country_code: str
    :param type: The type of the waypoint
    :type type: str
    :param name: The name of the waypoint
    :type name: str
    :param icao_code: The ICAO code of the waypoint
    :type icao_code: str
    :param usage_code: The usage code of the waypoint
    :type usage_code: str
    :param latitude: The latitude of the waypoint
    :type latitude: float
    :param longitude: The longitude of the waypoint
    :type longitude: float
    :param magnetic_variance: The magnetic variance from true north at the
     waypoint
    :type magnetic_variance: float
    :param navaid_id: The id of the associated navaid, if any
    :type navaid_id: int
    :param colocation_flag: Flag indicating whether or not the waypoint is
     colocated with the navaid
    :type colocation_flag: bool
    :param navaid_bearing: The magnetic bearing from the navaid to the
     waypoint
    :type navaid_bearing: float
    :param navaid_distance: The distance from the navaid to the waypoint
    :type navaid_distance: float
    :param dafif_id: The DAFIF text identifier of the waypoint
    :type dafif_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'airport_id': {'key': 'airportId', 'type': 'int'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'icao_code': {'key': 'icaoCode', 'type': 'str'},
        'usage_code': {'key': 'usageCode', 'type': 'str'},
        'latitude': {'key': 'latitude', 'type': 'float'},
        'longitude': {'key': 'longitude', 'type': 'float'},
        'magnetic_variance': {'key': 'magneticVariance', 'type': 'float'},
        'navaid_id': {'key': 'navaidId', 'type': 'int'},
        'colocation_flag': {'key': 'colocationFlag', 'type': 'bool'},
        'navaid_bearing': {'key': 'navaidBearing', 'type': 'float'},
        'navaid_distance': {'key': 'navaidDistance', 'type': 'float'},
        'dafif_id': {'key': 'dafifId', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, airport_id: int=None, country_code: str=None, type: str=None, name: str=None, icao_code: str=None, usage_code: str=None, latitude: float=None, longitude: float=None, magnetic_variance: float=None, navaid_id: int=None, colocation_flag: bool=None, navaid_bearing: float=None, navaid_distance: float=None, dafif_id: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoNavigationNavigationWaypoint, self).__init__(**kwargs)
        self.id = id
        self.airport_id = airport_id
        self.country_code = country_code
        self.type = type
        self.name = name
        self.icao_code = icao_code
        self.usage_code = usage_code
        self.latitude = latitude
        self.longitude = longitude
        self.magnetic_variance = magnetic_variance
        self.navaid_id = navaid_id
        self.colocation_flag = colocation_flag
        self.navaid_bearing = navaid_bearing
        self.navaid_distance = navaid_distance
        self.dafif_id = dafif_id
