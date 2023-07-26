# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoExportServiceServiceStatus(Model):
    """Contains status/count information for an export service.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The unique identifier of the export service to which
     this status information belongs
    :type id: str
    :param enabled: Required. Whether the service is currently enabled
    :type enabled: bool
    :param exports_waiting: The count of exports waiting to be processed
    :type exports_waiting: int
    :param exports_pending: The count of exports currently processing
    :type exports_pending: int
    :param exports_processed: The count of exports successfully processed
    :type exports_processed: int
    :param exports_failed: The count of exports that failed processing
    :type exports_failed: int
    :param last_dispatched_time: The last time that an export job was
     dispatched for processing
    :type last_dispatched_time: datetime
    :param last_successful_time: The last time an export completed
     successfully
    :type last_successful_time: datetime
    :param last_unsuccessful_time: The last time an export failed to process
    :type last_unsuccessful_time: datetime
    :param estimated_completion_time: The estimated completion time for all
     waiting exports
    :type estimated_completion_time: datetime
    """

    _validation = {
        'id': {'required': True},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'exports_waiting': {'key': 'exportsWaiting', 'type': 'int'},
        'exports_pending': {'key': 'exportsPending', 'type': 'int'},
        'exports_processed': {'key': 'exportsProcessed', 'type': 'int'},
        'exports_failed': {'key': 'exportsFailed', 'type': 'int'},
        'last_dispatched_time': {'key': 'lastDispatchedTime', 'type': 'iso-8601'},
        'last_successful_time': {'key': 'lastSuccessfulTime', 'type': 'iso-8601'},
        'last_unsuccessful_time': {'key': 'lastUnsuccessfulTime', 'type': 'iso-8601'},
        'estimated_completion_time': {'key': 'estimatedCompletionTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoExportServiceServiceStatus, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.enabled = kwargs.get('enabled', None)
        self.exports_waiting = kwargs.get('exports_waiting', None)
        self.exports_pending = kwargs.get('exports_pending', None)
        self.exports_processed = kwargs.get('exports_processed', None)
        self.exports_failed = kwargs.get('exports_failed', None)
        self.last_dispatched_time = kwargs.get('last_dispatched_time', None)
        self.last_successful_time = kwargs.get('last_successful_time', None)
        self.last_unsuccessful_time = kwargs.get('last_unsuccessful_time', None)
        self.estimated_completion_time = kwargs.get('estimated_completion_time', None)