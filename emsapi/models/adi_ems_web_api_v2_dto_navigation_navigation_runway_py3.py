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

    def __init__(self, *, id: int=None, airport_id: int=None, string: str=None, length: float=None, width: float=None, opposite_id: int=None, is_parallel: bool=None, heading_true: float=None, heading_magnetic: float=None, takeoff_distance: float=None, landing_distance: float=None, latitude_start: float=None, latitude_end: float=None, longitude_start: float=None, longitude_end: float=None, altitude_start: float=None, altitude_end: float=None, slope: float=None, threshold_displaced: float=None, threshold_latitude: float=None, threshold_longitude: float=None, threshold_elevation: float=None, threshold_cross_height: float=None, threshold_to_glideslope_distance: float=None, lighting: str=None, glideslope_angle: float=None, glideslope_latitude: float=None, glideslope_longitude: float=None, glideslope_altitude: float=None, localizer_width: float=None, localizer_navaid: int=None, localizer_frequency: float=None, backcourse_localizer_frequency: float=None, ils_bearing_course: float=None, dme_navaid: int=None, dme_bias: float=None, inner_marker_latitude: float=None, inner_marker_longitude: float=None, inner_marker_altitude: float=None, middle_marker_navaid: int=None, middle_marker_latitude: float=None, middle_marker_longitude: float=None, middle_marker_altitude: float=None, outer_marker_navaid: float=None, outer_marker_latitude: float=None, outer_marker_longitude: float=None, outer_marker_altitude: float=None, locator_navaid: int=None, locator_latitude: float=None, locator_longitude: float=None, locator_altitude: float=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoNavigationNavigationRunway, self).__init__(**kwargs)
        self.id = id
        self.airport_id = airport_id
        self.string = string
        self.length = length
        self.width = width
        self.opposite_id = opposite_id
        self.is_parallel = is_parallel
        self.heading_true = heading_true
        self.heading_magnetic = heading_magnetic
        self.takeoff_distance = takeoff_distance
        self.landing_distance = landing_distance
        self.latitude_start = latitude_start
        self.latitude_end = latitude_end
        self.longitude_start = longitude_start
        self.longitude_end = longitude_end
        self.altitude_start = altitude_start
        self.altitude_end = altitude_end
        self.slope = slope
        self.threshold_displaced = threshold_displaced
        self.threshold_latitude = threshold_latitude
        self.threshold_longitude = threshold_longitude
        self.threshold_elevation = threshold_elevation
        self.threshold_cross_height = threshold_cross_height
        self.threshold_to_glideslope_distance = threshold_to_glideslope_distance
        self.lighting = lighting
        self.glideslope_angle = glideslope_angle
        self.glideslope_latitude = glideslope_latitude
        self.glideslope_longitude = glideslope_longitude
        self.glideslope_altitude = glideslope_altitude
        self.localizer_width = localizer_width
        self.localizer_navaid = localizer_navaid
        self.localizer_frequency = localizer_frequency
        self.backcourse_localizer_frequency = backcourse_localizer_frequency
        self.ils_bearing_course = ils_bearing_course
        self.dme_navaid = dme_navaid
        self.dme_bias = dme_bias
        self.inner_marker_latitude = inner_marker_latitude
        self.inner_marker_longitude = inner_marker_longitude
        self.inner_marker_altitude = inner_marker_altitude
        self.middle_marker_navaid = middle_marker_navaid
        self.middle_marker_latitude = middle_marker_latitude
        self.middle_marker_longitude = middle_marker_longitude
        self.middle_marker_altitude = middle_marker_altitude
        self.outer_marker_navaid = outer_marker_navaid
        self.outer_marker_latitude = outer_marker_latitude
        self.outer_marker_longitude = outer_marker_longitude
        self.outer_marker_altitude = outer_marker_altitude
        self.locator_navaid = locator_navaid
        self.locator_latitude = locator_latitude
        self.locator_longitude = locator_longitude
        self.locator_altitude = locator_altitude
