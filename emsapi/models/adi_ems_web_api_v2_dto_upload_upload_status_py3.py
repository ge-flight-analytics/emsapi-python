# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoUploadUploadStatus(Model):
    """This is sent as a response to an upload transfer status request.

    :param current_count: The current number of bytes the server has received
     on this transfer.
    :type current_count: long
    :param state: The state of the upload. Possible values include:
     'transferring', 'waitingProcessing', 'processing', 'processedSuccess',
     'processedFailure', 'abandonedTransfer', 'abandonedProcessing', 'canceled'
    :type state: str or ~emsapi.models.enum
    :param message: Contains a user-readable message about the status of the
     transfer.
    :type message: str
    """

    _attribute_map = {
        'current_count': {'key': 'currentCount', 'type': 'long'},
        'state': {'key': 'state', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, current_count: int=None, state=None, message: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoUploadUploadStatus, self).__init__(**kwargs)
        self.current_count = current_count
        self.state = state
        self.message = message