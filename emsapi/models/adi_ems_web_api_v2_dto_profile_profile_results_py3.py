# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoProfileProfileResults(Model):
    """Encapsulates all the profile results for a flight.

    All required parameters must be populated in order to send to Azure.

    :param profile_version: Required. The integer version of the profile that
     was processed to generate the results,
     corresponding to an index in the array of version history entries for the
     profile
    :type profile_version: int
    :param parameter_filtering: Required. Indicates whether automatic
     parameter filtering was enabled when the profile was processed
    :type parameter_filtering: bool
    :param measurements: Required. The top-level, non-event-based, measurement
     results
    :type measurements:
     list[~emsapi.models.AdiEmsWebApiV2DtoProfileProfileResultValue]
    :param timepoints: Required. The top-level, non-event-based, timepoint
     results
    :type timepoints:
     list[~emsapi.models.AdiEmsWebApiV2DtoProfileProfileResultValue]
    :param events: Required. The event results detected in the flight
    :type events:
     list[~emsapi.models.AdiEmsWebApiV2DtoProfileProfileResultsEventRecord]
    """

    _validation = {
        'profile_version': {'required': True},
        'parameter_filtering': {'required': True},
        'measurements': {'required': True},
        'timepoints': {'required': True},
        'events': {'required': True},
    }

    _attribute_map = {
        'profile_version': {'key': 'profileVersion', 'type': 'int'},
        'parameter_filtering': {'key': 'parameterFiltering', 'type': 'bool'},
        'measurements': {'key': 'measurements', 'type': '[AdiEmsWebApiV2DtoProfileProfileResultValue]'},
        'timepoints': {'key': 'timepoints', 'type': '[AdiEmsWebApiV2DtoProfileProfileResultValue]'},
        'events': {'key': 'events', 'type': '[AdiEmsWebApiV2DtoProfileProfileResultsEventRecord]'},
    }

    def __init__(self, *, profile_version: int, parameter_filtering: bool, measurements, timepoints, events, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoProfileProfileResults, self).__init__(**kwargs)
        self.profile_version = profile_version
        self.parameter_filtering = parameter_filtering
        self.measurements = measurements
        self.timepoints = timepoints
        self.events = events
