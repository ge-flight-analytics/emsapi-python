# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoNavigationNavigationProcedure(Model):
    """Various pieces of information associated with a procedure.

    :param id: The unique identifier for this procedure
    :type id: int
    :param display_name: The String description formatted for display
     purposes.
     This should match what's displayed in the Approach Viewer
    :type display_name: str
    :param cycle_date: A text value representing the cycle date of the
     procedure
    :type cycle_date: str
    :param emergency_safe_altitude: The emergency safe altitude of the
     procedure
    :type emergency_safe_altitude: float
    :param string: A text identifier of the procedure
    :type string: str
    :param transitional_altitude: The transition altitude of the procedure
    :type transitional_altitude: float
    :param transitional_level: The transition level of the procedure
    :type transitional_level: float
    :param type: The type of the procedure
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'cycle_date': {'key': 'cycleDate', 'type': 'str'},
        'emergency_safe_altitude': {'key': 'emergencySafeAltitude', 'type': 'float'},
        'string': {'key': 'string', 'type': 'str'},
        'transitional_altitude': {'key': 'transitionalAltitude', 'type': 'float'},
        'transitional_level': {'key': 'transitionalLevel', 'type': 'float'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoNavigationNavigationProcedure, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.display_name = kwargs.get('display_name', None)
        self.cycle_date = kwargs.get('cycle_date', None)
        self.emergency_safe_altitude = kwargs.get('emergency_safe_altitude', None)
        self.string = kwargs.get('string', None)
        self.transitional_altitude = kwargs.get('transitional_altitude', None)
        self.transitional_level = kwargs.get('transitional_level', None)
        self.type = kwargs.get('type', None)
