# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoEmsProfileEmsProfile(Model):
    """Represents an APM (Automated Parameter Measurement) profile in an EMS
    system.

    All required parameters must be populated in order to send to Azure.

    :param profile_id: Required. The local identifier for a profile
    :type profile_id: int
    :param profile_guid: Required. The unique identifier of a profile in the
     system
    :type profile_guid: str
    :param profile_name: Required. The name of the profile
    :type profile_name: str
    :param library: Required. Flag for if a profile is a library profile
    :type library: bool
    :param current_version: Required. The version of the profile
    :type current_version: int
    :param path: Required. Path to the profile's location
    :type path: str
    """

    _validation = {
        'profile_id': {'required': True},
        'profile_guid': {'required': True},
        'profile_name': {'required': True},
        'library': {'required': True},
        'current_version': {'required': True},
        'path': {'required': True},
    }

    _attribute_map = {
        'profile_id': {'key': 'profileId', 'type': 'int'},
        'profile_guid': {'key': 'profileGuid', 'type': 'str'},
        'profile_name': {'key': 'profileName', 'type': 'str'},
        'library': {'key': 'library', 'type': 'bool'},
        'current_version': {'key': 'currentVersion', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoEmsProfileEmsProfile, self).__init__(**kwargs)
        self.profile_id = kwargs.get('profile_id', None)
        self.profile_guid = kwargs.get('profile_guid', None)
        self.profile_name = kwargs.get('profile_name', None)
        self.library = kwargs.get('library', None)
        self.current_version = kwargs.get('current_version', None)
        self.path = kwargs.get('path', None)
