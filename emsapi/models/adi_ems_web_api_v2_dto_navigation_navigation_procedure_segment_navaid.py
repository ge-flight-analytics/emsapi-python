# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoNavigationNavigationProcedureSegmentNavaid(Model):
    """A single navaid associated with a procedure segment.

    :param navaid_id: The ID of the navaid referenced by this segment
    :type navaid_id: int
    :param bearing: The bearing to the navaid
    :type bearing: float
    :param distance: The distance to the navaid
    :type distance: float
    :param latitude: The latitude of the navaid
    :type latitude: float
    :param longitude: The longitude of the navaid
    :type longitude: float
    :param elevation: The elevation of the navaid
    :type elevation: float
    """

    _attribute_map = {
        'navaid_id': {'key': 'navaidId', 'type': 'int'},
        'bearing': {'key': 'bearing', 'type': 'float'},
        'distance': {'key': 'distance', 'type': 'float'},
        'latitude': {'key': 'latitude', 'type': 'float'},
        'longitude': {'key': 'longitude', 'type': 'float'},
        'elevation': {'key': 'elevation', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoNavigationNavigationProcedureSegmentNavaid, self).__init__(**kwargs)
        self.navaid_id = kwargs.get('navaid_id', None)
        self.bearing = kwargs.get('bearing', None)
        self.distance = kwargs.get('distance', None)
        self.latitude = kwargs.get('latitude', None)
        self.longitude = kwargs.get('longitude', None)
        self.elevation = kwargs.get('elevation', None)
