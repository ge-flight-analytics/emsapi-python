# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoUploadUploadResult(Model):
    """Summarizes the result of an upload operation.

    :param transfer_successful: If this is true, the transfer was successful
     and also the transferred data are intact.
     This includes things like verifying the integrity of zip archives, for the
     overall transfer
     completion
    :type transfer_successful: bool
    :param message: If there was an error, then the error message will
     describe it. In the case of success, there
     may also be a message here. This message will be suitable for display to a
     user
    :type message: str
    """

    _attribute_map = {
        'transfer_successful': {'key': 'transferSuccessful', 'type': 'bool'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, transfer_successful: bool=None, message: str=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoUploadUploadResult, self).__init__(**kwargs)
        self.transfer_successful = transfer_successful
        self.message = message
