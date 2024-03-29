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

    def __init__(self, *, creation_time=None, fleet=None, aircraft_id=None, aircraft_version=None, dafif_release=None, airport_takeoff=None, airport_landing=None, airport_takeoff_at_takeoff=None, airport_takeoff_at_midpoint=None, airport_takeoff_at_touchdown=None, airport_landing_at_takeoff=None, airport_landing_at_midpoint=None, airport_landing_at_touchdown=None, latitude_at_takeoff=None, latitude_at_midpoint=None, latitude_at_touchdown=None, longitude_at_takeoff=None, longitude_at_midpoint=None, longitude_at_touchdown=None, gmt_at_takeoff=None, gmt_at_midpoint=None, gmt_at_touchdown=None, day_at_takeoff=None, day_at_midpoint=None, day_at_touchdown=None, month_at_takeoff=None, month_at_midpoint=None, month_at_touchdown=None, year_at_takeoff=None, year_at_midpoint=None, year_at_touchdown=None, date_at_takeoff=None, date_at_midpoint=None, date_at_touchdown=None, flight_num_at_takeoff=None, flight_num_at_midpoint=None, flight_num_at_touchdown=None, flight_num1_at_takeoff=None, flight_num1_at_midpoint=None, flight_num1_at_touchdown=None, flight_num2_at_takeoff=None, flight_num2_at_midpoint=None, flight_num2_at_touchdown=None, other=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoIdentificationIdentification, self).__init__(**kwargs)
        self.creation_time = creation_time
        self.fleet = fleet
        self.aircraft_id = aircraft_id
        self.aircraft_version = aircraft_version
        self.dafif_release = dafif_release
        self.airport_takeoff = airport_takeoff
        self.airport_landing = airport_landing
        self.airport_takeoff_at_takeoff = airport_takeoff_at_takeoff
        self.airport_takeoff_at_midpoint = airport_takeoff_at_midpoint
        self.airport_takeoff_at_touchdown = airport_takeoff_at_touchdown
        self.airport_landing_at_takeoff = airport_landing_at_takeoff
        self.airport_landing_at_midpoint = airport_landing_at_midpoint
        self.airport_landing_at_touchdown = airport_landing_at_touchdown
        self.latitude_at_takeoff = latitude_at_takeoff
        self.latitude_at_midpoint = latitude_at_midpoint
        self.latitude_at_touchdown = latitude_at_touchdown
        self.longitude_at_takeoff = longitude_at_takeoff
        self.longitude_at_midpoint = longitude_at_midpoint
        self.longitude_at_touchdown = longitude_at_touchdown
        self.gmt_at_takeoff = gmt_at_takeoff
        self.gmt_at_midpoint = gmt_at_midpoint
        self.gmt_at_touchdown = gmt_at_touchdown
        self.day_at_takeoff = day_at_takeoff
        self.day_at_midpoint = day_at_midpoint
        self.day_at_touchdown = day_at_touchdown
        self.month_at_takeoff = month_at_takeoff
        self.month_at_midpoint = month_at_midpoint
        self.month_at_touchdown = month_at_touchdown
        self.year_at_takeoff = year_at_takeoff
        self.year_at_midpoint = year_at_midpoint
        self.year_at_touchdown = year_at_touchdown
        self.date_at_takeoff = date_at_takeoff
        self.date_at_midpoint = date_at_midpoint
        self.date_at_touchdown = date_at_touchdown
        self.flight_num_at_takeoff = flight_num_at_takeoff
        self.flight_num_at_midpoint = flight_num_at_midpoint
        self.flight_num_at_touchdown = flight_num_at_touchdown
        self.flight_num1_at_takeoff = flight_num1_at_takeoff
        self.flight_num1_at_midpoint = flight_num1_at_midpoint
        self.flight_num1_at_touchdown = flight_num1_at_touchdown
        self.flight_num2_at_takeoff = flight_num2_at_takeoff
        self.flight_num2_at_midpoint = flight_num2_at_midpoint
        self.flight_num2_at_touchdown = flight_num2_at_touchdown
        self.other = other
