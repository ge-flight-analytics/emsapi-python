# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoProfileProcessingInformation(Model):
    """Encapsulates information about processing.

    All required parameters must be populated in order to send to Azure.

    :param processing_state: Required. The state of the processing.
    :type processing_state: str
    :param processed_date: Required. The date and time that the processing
     occurred (UTC).
    :type processed_date: datetime
    :param retry_count: Required. The retry count.
    :type retry_count: int
    :param worker_cpu_time: Required. The worker cpu time of the processing in
     seconds.
    :type worker_cpu_time: float
    :param worker_wall_time: Required. The worker wall time of the processing
     in seconds.
    :type worker_wall_time: float
    :param total_wall_time: Required. The total wall time of the processing in
     seconds.
    :type total_wall_time: float
    :param is_failure: Required. Whether it is a failure.
    :type is_failure: bool
    :param failure_type: Required. The failure type.
    :type failure_type: int
    :param failure_name: Required. The failure name.
    :type failure_name: str
    """

    _validation = {
        'processing_state': {'required': True},
        'processed_date': {'required': True},
        'retry_count': {'required': True},
        'worker_cpu_time': {'required': True},
        'worker_wall_time': {'required': True},
        'total_wall_time': {'required': True},
        'is_failure': {'required': True},
        'failure_type': {'required': True},
        'failure_name': {'required': True},
    }

    _attribute_map = {
        'processing_state': {'key': 'processingState', 'type': 'str'},
        'processed_date': {'key': 'processedDate', 'type': 'iso-8601'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'worker_cpu_time': {'key': 'workerCpuTime', 'type': 'float'},
        'worker_wall_time': {'key': 'workerWallTime', 'type': 'float'},
        'total_wall_time': {'key': 'totalWallTime', 'type': 'float'},
        'is_failure': {'key': 'isFailure', 'type': 'bool'},
        'failure_type': {'key': 'failureType', 'type': 'int'},
        'failure_name': {'key': 'failureName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoProfileProcessingInformation, self).__init__(**kwargs)
        self.processing_state = kwargs.get('processing_state', None)
        self.processed_date = kwargs.get('processed_date', None)
        self.retry_count = kwargs.get('retry_count', None)
        self.worker_cpu_time = kwargs.get('worker_cpu_time', None)
        self.worker_wall_time = kwargs.get('worker_wall_time', None)
        self.total_wall_time = kwargs.get('total_wall_time', None)
        self.is_failure = kwargs.get('is_failure', None)
        self.failure_type = kwargs.get('failure_type', None)
        self.failure_name = kwargs.get('failure_name', None)
