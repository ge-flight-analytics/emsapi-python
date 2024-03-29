# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoNavigationNavigationRunway(Model):
    """Various pieces of information associated with a runway.

    :param id: The unique identifier for the runway
    :type id: int
    :param airport_id: The unique identifier of the airport for this runway
    :type airport_id: int
    :param string: A text value associated with the runway
    :type string: str
    :param length: The length of the runway
    :type length: float
    :param width: The width of the runway
    :type width: float
    :param opposite_id: The dafif id of the reciprocal runway (i.e. landing in
     the opposite direction on this runway)
    :type opposite_id: int
    :param is_parallel: Whether the runway is parallel
    :type is_parallel: bool
    :param heading_true: The true heading of the runway
    :type heading_true: float
    :param heading_magnetic: The magnetic heading of the runway
    :type heading_magnetic: float
    :param takeoff_distance: The takeoff distance of the runway
    :type takeoff_distance: float
    :param landing_distance: The landing distance of the runway
    :type landing_distance: float
    :param latitude_start: The runway's starting latitude
    :type latitude_start: float
    :param latitude_end: The runway's ending latitude
    :type latitude_end: float
    :param longitude_start: The runway's starting longitude
    :type longitude_start: float
    :param longitude_end: The runway's ending longitude
    :type longitude_end: float
    :param altitude_start: The runway's starting altitude
    :type altitude_start: float
    :param altitude_end: The runway's ending altitude
    :type altitude_end: float
    :param slope: The slope of the runway
    :type slope: float
    :param threshold_displaced: The threshold displaced value associated with
     the runway
    :type threshold_displaced: float
    :param threshold_latitude: The threshold latitude value associated with
     the runway
    :type threshold_latitude: float
    :param threshold_longitude: The threshold longitude value associated with
     the runway
    :type threshold_longitude: float
    :param threshold_elevation: The threshold elevation value associated with
     the runway
    :type threshold_elevation: float
    :param threshold_cross_height: The threshold crossheight value associated
     with the runway
    :type threshold_cross_height: float
    :param threshold_to_glideslope_distance: The threshold to glideslope
     distance associated with the runway
    :type threshold_to_glideslope_distance: float
    :param lighting: Bitflags indicating the available lighting for the runway
    :type lighting: str
    :param glideslope_angle: The glideslope angle value associated with the
     runway
    :type glideslope_angle: float
    :param glideslope_latitude: The glideslope latitude value associated with
     the runway
    :type glideslope_latitude: float
    :param glideslope_longitude: The glideslope longitude value associated
     with the runway
    :type glideslope_longitude: float
    :param glideslope_altitude: The glideslope altitude value associated with
     the runway
    :type glideslope_altitude: float
    :param localizer_width: The localizer width value associated with the
     runway
    :type localizer_width: float
    :param localizer_navaid: The navaid id of the localizer navaid
    :type localizer_navaid: int
    :param localizer_frequency: The localizer frequency value associated with
     the runway
    :type localizer_frequency: float
    :param backcourse_localizer_frequency: The backcourse localizer frequency
     value associated with the runway
    :type backcourse_localizer_frequency: float
    :param ils_bearing_course: The magnetic heading to fly the ILS
    :type ils_bearing_course: float
    :param dme_navaid: The navid id of the localizer dme
    :type dme_navaid: int
    :param dme_bias: The DME bias for the runway (the distance in NM from the
     DME to the landing threshold)
    :type dme_bias: float
    :param inner_marker_latitude: The inner marker latitude value associated
     with the runway
    :type inner_marker_latitude: float
    :param inner_marker_longitude: The inner marker longitude value associated
     with the runway
    :type inner_marker_longitude: float
    :param inner_marker_altitude: The inner marker altitude value associated
     with the runway
    :type inner_marker_altitude: float
    :param middle_marker_navaid: The navaid id of the middle marker, if any
    :type middle_marker_navaid: int
    :param middle_marker_latitude: The middle marker latitude value associated
     with the runway
    :type middle_marker_latitude: float
    :param middle_marker_longitude: The middle marker longitude value
     associated with the runway
    :type middle_marker_longitude: float
    :param middle_marker_altitude: The middle marker altitude value associated
     with the runway
    :type middle_marker_altitude: float
    :param outer_marker_navaid: The navaid id of the outer marker, if any
    :type outer_marker_navaid: float
    :param outer_marker_latitude: The outer marker latitude value associated
     with the runway
    :type outer_marker_latitude: float
    :param outer_marker_longitude: The outer marker longitude value associated
     with the runway
    :type outer_marker_longitude: float
    :param outer_marker_altitude: The outer marker altitude value associated
     with the runway
    :type outer_marker_altitude: float
    :param locator_navaid: The navaid id of the compass locator, if any
    :type locator_navaid: int
    :param locator_latitude: The locator latitude value associated with the
     runway
    :type locator_latitude: float
    :param locator_longitude: The locator longitude value associated with the
     runway
    :type locator_longitude: float
    :param locator_altitude: The locator altitude value associated with the
     runway
    :type locator_altitude: float
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'airport_id': {'key': 'airportId', 'type': 'int'},
        'string': {'key': 'string', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'width': {'key': 'width', 'type': 'float'},
        'opposite_id': {'key': 'oppositeId', 'type': 'int'},
        'is_parallel': {'key': 'isParallel', 'type': 'bool'},
        'heading_true': {'key': 'headingTrue', 'type': 'float'},
        'heading_magnetic': {'key': 'headingMagnetic', 'type': 'float'},
        'takeoff_distance': {'key': 'takeoffDistance', 'type': 'float'},
        'landing_distance': {'key': 'landingDistance', 'type': 'float'},
        'latitude_start': {'key': 'latitudeStart', 'type': 'float'},
        'latitude_end': {'key': 'latitudeEnd', 'type': 'float'},
        'longitude_start': {'key': 'longitudeStart', 'type': 'float'},
        'longitude_end': {'key': 'longitudeEnd', 'type': 'float'},
        'altitude_start': {'key': 'altitudeStart', 'type': 'float'},
        'altitude_end': {'key': 'altitudeEnd', 'type': 'float'},
        'slope': {'key': 'slope', 'type': 'float'},
        'threshold_displaced': {'key': 'thresholdDisplaced', 'type': 'float'},
        'threshold_latitude': {'key': 'thresholdLatitude', 'type': 'float'},
        'threshold_longitude': {'key': 'thresholdLongitude', 'type': 'float'},
        'threshold_elevation': {'key': 'thresholdElevation', 'type': 'float'},
        'threshold_cross_height': {'key': 'thresholdCrossHeight', 'type': 'float'},
        'threshold_to_glideslope_distance': {'key': 'thresholdToGlideslopeDistance', 'type': 'float'},
        'lighting': {'key': 'lighting', 'type': 'str'},
        'glideslope_angle': {'key': 'glideslopeAngle', 'type': 'float'},
        'glideslope_latitude': {'key': 'glideslopeLatitude', 'type': 'float'},
        'glideslope_longitude': {'key': 'glideslopeLongitude', 'type': 'float'},
        'glideslope_altitude': {'key': 'glideslopeAltitude', 'type': 'float'},
        'localizer_width': {'key': 'localizerWidth', 'type': 'float'},
        'localizer_navaid': {'key': 'localizerNavaid', 'type': 'int'},
        'localizer_frequency': {'key': 'localizerFrequency', 'type': 'float'},
        'backcourse_localizer_frequency': {'key': 'backcourseLocalizerFrequency', 'type': 'float'},
        'ils_bearing_course': {'key': 'ilsBearingCourse', 'type': 'float'},
        'dme_navaid': {'key': 'dmeNavaid', 'type': 'int'},
        'dme_bias': {'key': 'dmeBias', 'type': 'float'},
        'inner_marker_latitude': {'key': 'innerMarkerLatitude', 'type': 'float'},
        'inner_marker_longitude': {'key': 'innerMarkerLongitude', 'type': 'float'},
        'inner_marker_altitude': {'key': 'innerMarkerAltitude', 'type': 'float'},
        'middle_marker_navaid': {'key': 'middleMarkerNavaid', 'type': 'int'},
        'middle_marker_latitude': {'key': 'middleMarkerLatitude', 'type': 'float'},
        'middle_marker_longitude': {'key': 'middleMarkerLongitude', 'type': 'float'},
        'middle_marker_altitude': {'key': 'middleMarkerAltitude', 'type': 'float'},
        'outer_marker_navaid': {'key': 'outerMarkerNavaid', 'type': 'float'},
        'outer_marker_latitude': {'key': 'outerMarkerLatitude', 'type': 'float'},
        'outer_marker_longitude': {'key': 'outerMarkerLongitude', 'type': 'float'},
        'outer_marker_altitude': {'key': 'outerMarkerAltitude', 'type': 'float'},
        'locator_navaid': {'key': 'locatorNavaid', 'type': 'int'},
        'locator_latitude': {'key': 'locatorLatitude', 'type': 'float'},
        'locator_longitude': {'key': 'locatorLongitude', 'type': 'float'},
        'locator_altitude': {'key': 'locatorAltitude', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoNavigationNavigationRunway, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.airport_id = kwargs.get('airport_id', None)
        self.string = kwargs.get('string', None)
        self.length = kwargs.get('length', None)
        self.width = kwargs.get('width', None)
        self.opposite_id = kwargs.get('opposite_id', None)
        self.is_parallel = kwargs.get('is_parallel', None)
        self.heading_true = kwargs.get('heading_true', None)
        self.heading_magnetic = kwargs.get('heading_magnetic', None)
        self.takeoff_distance = kwargs.get('takeoff_distance', None)
        self.landing_distance = kwargs.get('landing_distance', None)
        self.latitude_start = kwargs.get('latitude_start', None)
        self.latitude_end = kwargs.get('latitude_end', None)
        self.longitude_start = kwargs.get('longitude_start', None)
        self.longitude_end = kwargs.get('longitude_end', None)
        self.altitude_start = kwargs.get('altitude_start', None)
        self.altitude_end = kwargs.get('altitude_end', None)
        self.slope = kwargs.get('slope', None)
        self.threshold_displaced = kwargs.get('threshold_displaced', None)
        self.threshold_latitude = kwargs.get('threshold_latitude', None)
        self.threshold_longitude = kwargs.get('threshold_longitude', None)
        self.threshold_elevation = kwargs.get('threshold_elevation', None)
        self.threshold_cross_height = kwargs.get('threshold_cross_height', None)
        self.threshold_to_glideslope_distance = kwargs.get('threshold_to_glideslope_distance', None)
        self.lighting = kwargs.get('lighting', None)
        self.glideslope_angle = kwargs.get('glideslope_angle', None)
        self.glideslope_latitude = kwargs.get('glideslope_latitude', None)
        self.glideslope_longitude = kwargs.get('glideslope_longitude', None)
        self.glideslope_altitude = kwargs.get('glideslope_altitude', None)
        self.localizer_width = kwargs.get('localizer_width', None)
        self.localizer_navaid = kwargs.get('localizer_navaid', None)
        self.localizer_frequency = kwargs.get('localizer_frequency', None)
        self.backcourse_localizer_frequency = kwargs.get('backcourse_localizer_frequency', None)
        self.ils_bearing_course = kwargs.get('ils_bearing_course', None)
        self.dme_navaid = kwargs.get('dme_navaid', None)
        self.dme_bias = kwargs.get('dme_bias', None)
        self.inner_marker_latitude = kwargs.get('inner_marker_latitude', None)
        self.inner_marker_longitude = kwargs.get('inner_marker_longitude', None)
        self.inner_marker_altitude = kwargs.get('inner_marker_altitude', None)
        self.middle_marker_navaid = kwargs.get('middle_marker_navaid', None)
        self.middle_marker_latitude = kwargs.get('middle_marker_latitude', None)
        self.middle_marker_longitude = kwargs.get('middle_marker_longitude', None)
        self.middle_marker_altitude = kwargs.get('middle_marker_altitude', None)
        self.outer_marker_navaid = kwargs.get('outer_marker_navaid', None)
        self.outer_marker_latitude = kwargs.get('outer_marker_latitude', None)
        self.outer_marker_longitude = kwargs.get('outer_marker_longitude', None)
        self.outer_marker_altitude = kwargs.get('outer_marker_altitude', None)
        self.locator_navaid = kwargs.get('locator_navaid', None)
        self.locator_latitude = kwargs.get('locator_latitude', None)
        self.locator_longitude = kwargs.get('locator_longitude', None)
        self.locator_altitude = kwargs.get('locator_altitude', None)
