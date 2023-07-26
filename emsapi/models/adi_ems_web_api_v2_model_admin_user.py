# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2ModelAdminUser(Model):
    """Represents a user account that can be used to access the website.

    All required parameters must be populated in order to send to Azure.

    :param id: The unique integer identifier of the user.
    :type id: int
    :param username: Required. The Active Directory username of the user,
     typically in the form of "domain\\user.name". If not in an
     environment with multiple domains, the domain name is not needed.
    :type username: str
    :param lockout_policy_enabled: Indicates whether the account lockout
     policy applies to this user, causing them to be locked out of the
     application for a configured amount of time after failed login attempts.
    :type lockout_policy_enabled: bool
    :param roles: The list of roles to which the user is a member.
    :type roles: list[str]
    :param tableau_username: The Tableau username to which this user is
     linked. This user name is only needed if different than the user
     name.
    :type tableau_username: str
    :param last_login: A read-only value indicating the last time the user
     logged into the application.
    :type last_login: datetime
    :param lockout_end_date_utc: A read-only value indicating the time that
     the user will no longer be locked out. Null if the user is not
     currently locked out.
    :type lockout_end_date_utc: datetime
    :param access_failed_count: A read-only value indicating the number of
     times the user failed to login.
    :type access_failed_count: int
    """

    _validation = {
        'username': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'username': {'key': 'username', 'type': 'str'},
        'lockout_policy_enabled': {'key': 'lockoutPolicyEnabled', 'type': 'bool'},
        'roles': {'key': 'roles', 'type': '[str]'},
        'tableau_username': {'key': 'tableauUsername', 'type': 'str'},
        'last_login': {'key': 'lastLogin', 'type': 'iso-8601'},
        'lockout_end_date_utc': {'key': 'lockoutEndDateUtc', 'type': 'iso-8601'},
        'access_failed_count': {'key': 'accessFailedCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2ModelAdminUser, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.username = kwargs.get('username', None)
        self.lockout_policy_enabled = kwargs.get('lockout_policy_enabled', None)
        self.roles = kwargs.get('roles', None)
        self.tableau_username = kwargs.get('tableau_username', None)
        self.last_login = kwargs.get('last_login', None)
        self.lockout_end_date_utc = kwargs.get('lockout_end_date_utc', None)
        self.access_failed_count = kwargs.get('access_failed_count', None)
