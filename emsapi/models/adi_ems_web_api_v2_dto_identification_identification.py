# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoIdentificationIdentification(Model):
    """Represents the identification information for a flight.

    :param creation_time: The creation time of the identification record
    :type creation_time:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param fleet: The fleet name that this flight is associated with
    :type fleet:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param aircraft_id: The aircraft identifier. This could be the tail number
     or some other identifier
    :type aircraft_id:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param aircraft_version: The aircraft version. This could be nose number
     or some other value
    :type aircraft_version:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param dafif_release: The DAFIF release associated with this flight
    :type dafif_release:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param airport_takeoff: The takeoff airport for the flight
    :type airport_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param airport_landing: The landing airport for the flight
    :type airport_landing:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param airport_takeoff_at_takeoff: The takeoff airport recorded at takeoff
     of the flight
    :type airport_takeoff_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param airport_takeoff_at_midpoint: The takeoff airport recorded at the
     midpoint of the flight
    :type airport_takeoff_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param airport_takeoff_at_touchdown: The takeoff airport recorded at
     touchdown of the flight
    :type airport_takeoff_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param airport_landing_at_takeoff: The landing airport recorded at takeoff
     of the flight
    :type airport_landing_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param airport_landing_at_midpoint: The landing airport recorded at the
     midpoint of the flight
    :type airport_landing_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param airport_landing_at_touchdown: The landing airport recorded at
     touchdown of the flight
    :type airport_landing_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param latitude_at_takeoff: The latitude recorded at takeoff of the flight
    :type latitude_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param latitude_at_midpoint: The latitude recorded at the midpoint of the
     flight
    :type latitude_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param latitude_at_touchdown: The latitude recorded at touchdown of the
     flight
    :type latitude_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param longitude_at_takeoff: The longitude recorded at takeoff of the
     flight
    :type longitude_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param longitude_at_midpoint: The longitude recorded at midpoint of the
     flight
    :type longitude_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param longitude_at_touchdown: The longitude recorded at touchdown of the
     flight
    :type longitude_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param gmt_at_takeoff: The GMT recorded at takeoff of the flight
    :type gmt_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param gmt_at_midpoint: The GMT recorded at the midpoint of the flight
    :type gmt_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param gmt_at_touchdown: The GMT recorded at touchdown of the flight
    :type gmt_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param day_at_takeoff: The day recorded at takeoff of the flight
    :type day_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param day_at_midpoint: The day recorded at the midpoint of the flight
    :type day_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param day_at_touchdown: The day recorded at touchdown of the flight
    :type day_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param month_at_takeoff: The month recorded at takeoff of the flight
    :type month_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param month_at_midpoint: The month recorded at midpoint of the flight
    :type month_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param month_at_touchdown: The month recorded at touchdown of the flight
    :type month_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param year_at_takeoff: The year recorded at takeoff of the flight
    :type year_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param year_at_midpoint: The year recorded at midpoint of the flight
    :type year_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param year_at_touchdown: The year recorded at touchdown of the flight
    :type year_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param date_at_takeoff: The date recorded at takeoff of the flight
    :type date_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param date_at_midpoint: The date recorded at the midpoint of the flight
    :type date_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param date_at_touchdown: The date recorded at touchdown of the flight
    :type date_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num_at_takeoff: The flight number processed at takeoff of
     the flight
    :type flight_num_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num_at_midpoint: The flight number processed at the midpoint
     of the flight
    :type flight_num_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num_at_touchdown: The flight number processed at touchdown
     of the flight
    :type flight_num_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num1_at_takeoff: The flight number recorded at takeoff of
     the flight
    :type flight_num1_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num1_at_midpoint: The flight number recorded at the midpoint
     of the flight
    :type flight_num1_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num1_at_touchdown: The flight number recorded at touchdown
     of the flight
    :type flight_num1_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num2_at_takeoff: The secondary flight recorded at takeoff of
     the flight
    :type flight_num2_at_takeoff:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num2_at_midpoint: The secondary flight recorded at the
     midpoint of the flight
    :type flight_num2_at_midpoint:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param flight_num2_at_touchdown: The secondary flight number recorded at
     touchdown of the flight
    :type flight_num2_at_touchdown:
     ~emsapi.models.AdiEmsWebApiV2DtoIdentificationIdentificationField
    :param other: Any other identificaton fields
    :type other: dict[str, str]
    """

    _attribute_map = {
        'creation_time': {'key': 'creationTime', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'fleet': {'key': 'fleet', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'aircraft_id': {'key': 'aircraftId', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'aircraft_version': {'key': 'aircraftVersion', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'dafif_release': {'key': 'dafifRelease', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'airport_takeoff': {'key': 'airportTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'airport_landing': {'key': 'airportLanding', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'airport_takeoff_at_takeoff': {'key': 'airportTakeoffAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'airport_takeoff_at_midpoint': {'key': 'airportTakeoffAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'airport_takeoff_at_touchdown': {'key': 'airportTakeoffAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'airport_landing_at_takeoff': {'key': 'airportLandingAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'airport_landing_at_midpoint': {'key': 'airportLandingAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'airport_landing_at_touchdown': {'key': 'airportLandingAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'latitude_at_takeoff': {'key': 'latitudeAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'latitude_at_midpoint': {'key': 'latitudeAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'latitude_at_touchdown': {'key': 'latitudeAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'longitude_at_takeoff': {'key': 'longitudeAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'longitude_at_midpoint': {'key': 'longitudeAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'longitude_at_touchdown': {'key': 'longitudeAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'gmt_at_takeoff': {'key': 'gmtAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'gmt_at_midpoint': {'key': 'gmtAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'gmt_at_touchdown': {'key': 'gmtAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'day_at_takeoff': {'key': 'dayAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'day_at_midpoint': {'key': 'dayAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'day_at_touchdown': {'key': 'dayAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'month_at_takeoff': {'key': 'monthAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'month_at_midpoint': {'key': 'monthAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'month_at_touchdown': {'key': 'monthAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'year_at_takeoff': {'key': 'yearAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'year_at_midpoint': {'key': 'yearAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'year_at_touchdown': {'key': 'yearAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'date_at_takeoff': {'key': 'dateAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'date_at_midpoint': {'key': 'dateAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'date_at_touchdown': {'key': 'dateAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num_at_takeoff': {'key': 'flightNumAtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num_at_midpoint': {'key': 'flightNumAtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num_at_touchdown': {'key': 'flightNumAtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num1_at_takeoff': {'key': 'flightNum1AtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num1_at_midpoint': {'key': 'flightNum1AtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num1_at_touchdown': {'key': 'flightNum1AtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num2_at_takeoff': {'key': 'flightNum2AtTakeoff', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num2_at_midpoint': {'key': 'flightNum2AtMidpoint', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'flight_num2_at_touchdown': {'key': 'flightNum2AtTouchdown', 'type': 'AdiEmsWebApiV2DtoIdentificationIdentificationField'},
        'other': {'key': 'other', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoIdentificationIdentification, self).__init__(**kwargs)
        self.creation_time = kwargs.get('creation_time', None)
        self.fleet = kwargs.get('fleet', None)
        self.aircraft_id = kwargs.get('aircraft_id', None)
        self.aircraft_version = kwargs.get('aircraft_version', None)
        self.dafif_release = kwargs.get('dafif_release', None)
        self.airport_takeoff = kwargs.get('airport_takeoff', None)
        self.airport_landing = kwargs.get('airport_landing', None)
        self.airport_takeoff_at_takeoff = kwargs.get('airport_takeoff_at_takeoff', None)
        self.airport_takeoff_at_midpoint = kwargs.get('airport_takeoff_at_midpoint', None)
        self.airport_takeoff_at_touchdown = kwargs.get('airport_takeoff_at_touchdown', None)
        self.airport_landing_at_takeoff = kwargs.get('airport_landing_at_takeoff', None)
        self.airport_landing_at_midpoint = kwargs.get('airport_landing_at_midpoint', None)
        self.airport_landing_at_touchdown = kwargs.get('airport_landing_at_touchdown', None)
        self.latitude_at_takeoff = kwargs.get('latitude_at_takeoff', None)
        self.latitude_at_midpoint = kwargs.get('latitude_at_midpoint', None)
        self.latitude_at_touchdown = kwargs.get('latitude_at_touchdown', None)
        self.longitude_at_takeoff = kwargs.get('longitude_at_takeoff', None)
        self.longitude_at_midpoint = kwargs.get('longitude_at_midpoint', None)
        self.longitude_at_touchdown = kwargs.get('longitude_at_touchdown', None)
        self.gmt_at_takeoff = kwargs.get('gmt_at_takeoff', None)
        self.gmt_at_midpoint = kwargs.get('gmt_at_midpoint', None)
        self.gmt_at_touchdown = kwargs.get('gmt_at_touchdown', None)
        self.day_at_takeoff = kwargs.get('day_at_takeoff', None)
        self.day_at_midpoint = kwargs.get('day_at_midpoint', None)
        self.day_at_touchdown = kwargs.get('day_at_touchdown', None)
        self.month_at_takeoff = kwargs.get('month_at_takeoff', None)
        self.month_at_midpoint = kwargs.get('month_at_midpoint', None)
        self.month_at_touchdown = kwargs.get('month_at_touchdown', None)
        self.year_at_takeoff = kwargs.get('year_at_takeoff', None)
        self.year_at_midpoint = kwargs.get('year_at_midpoint', None)
        self.year_at_touchdown = kwargs.get('year_at_touchdown', None)
        self.date_at_takeoff = kwargs.get('date_at_takeoff', None)
        self.date_at_midpoint = kwargs.get('date_at_midpoint', None)
        self.date_at_touchdown = kwargs.get('date_at_touchdown', None)
        self.flight_num_at_takeoff = kwargs.get('flight_num_at_takeoff', None)
        self.flight_num_at_midpoint = kwargs.get('flight_num_at_midpoint', None)
        self.flight_num_at_touchdown = kwargs.get('flight_num_at_touchdown', None)
        self.flight_num1_at_takeoff = kwargs.get('flight_num1_at_takeoff', None)
        self.flight_num1_at_midpoint = kwargs.get('flight_num1_at_midpoint', None)
        self.flight_num1_at_touchdown = kwargs.get('flight_num1_at_touchdown', None)
        self.flight_num2_at_takeoff = kwargs.get('flight_num2_at_takeoff', None)
        self.flight_num2_at_midpoint = kwargs.get('flight_num2_at_midpoint', None)
        self.flight_num2_at_touchdown = kwargs.get('flight_num2_at_touchdown', None)
        self.other = kwargs.get('other', None)
