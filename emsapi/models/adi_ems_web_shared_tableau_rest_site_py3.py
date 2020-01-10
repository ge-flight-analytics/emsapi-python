# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebSharedTableauRestSite(Model):
    """AdiEmsWebSharedTableauRestSite.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param content_url:
    :type content_url: str
    :param admin_mode:
    :type admin_mode: str
    :param user_quota:
    :type user_quota: str
    :param storage_quota:
    :type storage_quota: str
    :param state:
    :type state: str
    :param status_reason:
    :type status_reason: str
    :param revision_history_enabled:
    :type revision_history_enabled: bool
    :param subscribe_others_enabled:
    :type subscribe_others_enabled: bool
    :param revision_limit:
    :type revision_limit: int
    :param guest_access_enabled:
    :type guest_access_enabled: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'admin_mode': {'key': 'adminMode', 'type': 'str'},
        'user_quota': {'key': 'userQuota', 'type': 'str'},
        'storage_quota': {'key': 'storageQuota', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'status_reason': {'key': 'statusReason', 'type': 'str'},
        'revision_history_enabled': {'key': 'revisionHistoryEnabled', 'type': 'bool'},
        'subscribe_others_enabled': {'key': 'subscribeOthersEnabled', 'type': 'bool'},
        'revision_limit': {'key': 'revisionLimit', 'type': 'int'},
        'guest_access_enabled': {'key': 'guestAccessEnabled', 'type': 'bool'},
    }

    def __init__(self, *, id: str=None, name: str=None, content_url: str=None, admin_mode: str=None, user_quota: str=None, storage_quota: str=None, state: str=None, status_reason: str=None, revision_history_enabled: bool=None, subscribe_others_enabled: bool=None, revision_limit: int=None, guest_access_enabled: bool=None, **kwargs) -> None:
        super(AdiEmsWebSharedTableauRestSite, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.content_url = content_url
        self.admin_mode = admin_mode
        self.user_quota = user_quota
        self.storage_quota = storage_quota
        self.state = state
        self.status_reason = status_reason
        self.revision_history_enabled = revision_history_enabled
        self.subscribe_others_enabled = subscribe_others_enabled
        self.revision_limit = revision_limit
        self.guest_access_enabled = guest_access_enabled