# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoNavigationNavigationNavaid(Model):
    """Various pieces of information associated with a waypoint.

    :param id: The unique identifier of the navaid.
    :type id: int
    :param callsign: The radio callsign of the navaid.
    :type callsign: str
    :param type: The navaid type.
    :type type: str
    :param country_code: The navaid's country code.
    :type country_code: str
    :param state_code: The navaid's state code.
    :type state_code: int
    :param name: The official name of the navaid.
    :type name: str
    :param frequency: The radio frequency of the navaid.
    :type frequency: float
    :param usage_code: The airspace structure in which the navaid is utilized
     (e.g. high, low, terminal, etc.)
    :type usage_code: str
    :param channel: The navaid's radio channel.
    :type channel: str
    :param radio_class_code: The radio class code of the navaid (e.g.
     low-power NDB, high-power NDB, etc)
    :type radio_class_code: str
    :param range: The effective range of the navaid in nautical miles.
    :type range: float
    :param latitude: The latitude of the navaid.
    :type latitude: float
    :param longitude: The longitude of the navaid.
    :type longitude: float
    :param elevation: The navaid's elevation.
    :type elevation: float
    :param magnetic_variance: The magnetic varation from true north at the
     navaid.
    :type magnetic_variance: float
    :param dme_latitude: The latitude of the DME equipment colocated with the
     navaid, if any.
    :type dme_latitude: float
    :param dme_longitude: The longitude of the DME equipment colocated with
     the navaid, if any.
    :type dme_longitude: float
    :param dme_elevation: The elevation of the DME equipment colocated with
     the navaid, if any.
    :type dme_elevation: float
    :param associated_airport: The airport code of the associated airport, if
     any.
    :type associated_airport: str
    :param status: The status of the navaid (e.g. in service, out of service,
     etc.)
    :type status: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'callsign': {'key': 'callsign', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'state_code': {'key': 'stateCode', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'frequency': {'key': 'frequency', 'type': 'float'},
        'usage_code': {'key': 'usageCode', 'type': 'str'},
        'channel': {'key': 'channel', 'type': 'str'},
        'radio_class_code': {'key': 'radioClassCode', 'type': 'str'},
        'range': {'key': 'range', 'type': 'float'},
        'latitude': {'key': 'latitude', 'type': 'float'},
        'longitude': {'key': 'longitude', 'type': 'float'},
        'elevation': {'key': 'elevation', 'type': 'float'},
        'magnetic_variance': {'key': 'magneticVariance', 'type': 'float'},
        'dme_latitude': {'key': 'dmeLatitude', 'type': 'float'},
        'dme_longitude': {'key': 'dmeLongitude', 'type': 'float'},
        'dme_elevation': {'key': 'dmeElevation', 'type': 'float'},
        'associated_airport': {'key': 'associatedAirport', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoNavigationNavigationNavaid, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.callsign = kwargs.get('callsign', None)
        self.type = kwargs.get('type', None)
        self.country_code = kwargs.get('country_code', None)
        self.state_code = kwargs.get('state_code', None)
        self.name = kwargs.get('name', None)
        self.frequency = kwargs.get('frequency', None)
        self.usage_code = kwargs.get('usage_code', None)
        self.channel = kwargs.get('channel', None)
        self.radio_class_code = kwargs.get('radio_class_code', None)
        self.range = kwargs.get('range', None)
        self.latitude = kwargs.get('latitude', None)
        self.longitude = kwargs.get('longitude', None)
        self.elevation = kwargs.get('elevation', None)
        self.magnetic_variance = kwargs.get('magnetic_variance', None)
        self.dme_latitude = kwargs.get('dme_latitude', None)
        self.dme_longitude = kwargs.get('dme_longitude', None)
        self.dme_elevation = kwargs.get('dme_elevation', None)
        self.associated_airport = kwargs.get('associated_airport', None)
        self.status = kwargs.get('status', None)
