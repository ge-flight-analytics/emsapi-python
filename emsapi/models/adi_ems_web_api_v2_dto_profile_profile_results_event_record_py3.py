# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoProfileProfileResultsEventRecord(Model):
    """Encapsulates information about an event result stored in the database.

    All required parameters must be populated in order to send to Azure.

    :param record_number: Required. The unique integer ID of the event in the
     database
    :type record_number: int
    :param event_type: Required. The unique ID of the event definition that
     generated the event
    :type event_type: int
    :param phase_of_flight: Required. The phase of flight where the event
     occurred (which is a value from the EMS phase of flight list)
    :type phase_of_flight: int
    :param severity: Required. The event severity (which is a value from the
     EMS severity list)
    :type severity: int
    :param status: Required. The status of the event (which is a value from
     the EMS status list). Typically this defaults to
     0 for new events, but in some data-merge scenarios we need to import a
     non-default value
     from a remote system
    :type status: int
    :param false_positive: Required. The false positive value for the event (a
     value from the EMS false positive list).
     Typically this defaults to 0 for new events, but in some data-merge
     scenarios we
     need to import a non-default value from a remote system
    :type false_positive: int
    :param start_time: The start offset for the event.
     This can be null for computed events where the timepoint or interval
     aren't set or don't resolve
    :type start_time: float
    :param end_time: The end offset for the event.
     This can be null for computed events where the timepoint or interval
     aren't set or don't resolve
    :type end_time: float
    :param global_measurements: Required. The global event measurement results
     (defined for all events)
    :type global_measurements:
     list[~emsapi.models.AdiEmsWebApiV2DtoProfileProfileResultValue]
    :param global_timepoints: Required. The global event timepoint results
     (defined for all events)
    :type global_timepoints:
     list[~emsapi.models.AdiEmsWebApiV2DtoProfileProfileResultValue]
    :param local_measurements: Required. The event-specific measurement
     results (different for each event type)
    :type local_measurements:
     list[~emsapi.models.AdiEmsWebApiV2DtoProfileProfileResultValue]
    :param local_timepoints: Required. The event-specific timepoint results
     (different for each event type)
    :type local_timepoints:
     list[~emsapi.models.AdiEmsWebApiV2DtoProfileProfileResultValue]
    :param comments: Required. The event comments. Usually this is empty, but
     it's required for some data-merge
     scenarios.
    :type comments:
     list[~emsapi.models.AdiEmsWebApiV2DtoProfileProfileResultComment]
    """

    _validation = {
        'record_number': {'required': True},
        'event_type': {'required': True},
        'phase_of_flight': {'required': True},
        'severity': {'required': True},
        'status': {'required': True},
        'false_positive': {'required': True},
        'global_measurements': {'required': True},
        'global_timepoints': {'required': True},
        'local_measurements': {'required': True},
        'local_timepoints': {'required': True},
        'comments': {'required': True},
    }

    _attribute_map = {
        'record_number': {'key': 'recordNumber', 'type': 'int'},
        'event_type': {'key': 'eventType', 'type': 'int'},
        'phase_of_flight': {'key': 'phaseOfFlight', 'type': 'int'},
        'severity': {'key': 'severity', 'type': 'int'},
        'status': {'key': 'status', 'type': 'int'},
        'false_positive': {'key': 'falsePositive', 'type': 'int'},
        'start_time': {'key': 'startTime', 'type': 'float'},
        'end_time': {'key': 'endTime', 'type': 'float'},
        'global_measurements': {'key': 'globalMeasurements', 'type': '[AdiEmsWebApiV2DtoProfileProfileResultValue]'},
        'global_timepoints': {'key': 'globalTimepoints', 'type': '[AdiEmsWebApiV2DtoProfileProfileResultValue]'},
        'local_measurements': {'key': 'localMeasurements', 'type': '[AdiEmsWebApiV2DtoProfileProfileResultValue]'},
        'local_timepoints': {'key': 'localTimepoints', 'type': '[AdiEmsWebApiV2DtoProfileProfileResultValue]'},
        'comments': {'key': 'comments', 'type': '[AdiEmsWebApiV2DtoProfileProfileResultComment]'},
    }

    def __init__(self, *, record_number: int, event_type: int, phase_of_flight: int, severity: int, status: int, false_positive: int, global_measurements, global_timepoints, local_measurements, local_timepoints, comments, start_time: float=None, end_time: float=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoProfileProfileResultsEventRecord, self).__init__(**kwargs)
        self.record_number = record_number
        self.event_type = event_type
        self.phase_of_flight = phase_of_flight
        self.severity = severity
        self.status = status
        self.false_positive = false_positive
        self.start_time = start_time
        self.end_time = end_time
        self.global_measurements = global_measurements
        self.global_timepoints = global_timepoints
        self.local_measurements = local_measurements
        self.local_timepoints = local_timepoints
        self.comments = comments
