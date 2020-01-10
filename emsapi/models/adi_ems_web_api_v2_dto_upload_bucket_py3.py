# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoUploadBucket(Model):
    """The name and description of an upload bucket.

    :param name: The name of the bucket. This is unique
    :type name: str
    :param description: Description of the bucket
    :type description: str
    :param associated_ems_system: The EmsSystem that this bucket is associated
     with. This is used for determining
     the EMS Processing status when using the processing status API
    :type associated_ems_system: ~emsapi.models.AdiEmsWebDataModelEmsSystem
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'associated_ems_system': {'key': 'associatedEmsSystem', 'type': 'AdiEmsWebDataModelEmsSystem'},
    }

    def __init__(self, *, name: str=None, description: str=None, associated_ems_system=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoUploadBucket, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.associated_ems_system = associated_ems_system
