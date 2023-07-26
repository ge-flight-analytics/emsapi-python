# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAlertGetActivity(Model):
    """Output type for getting the activity of an alert, and returned from a call
    to add alert trigger history.

    :param recorded_at: The timestamp of when the activity record was recorded
     on the server.
    :type recorded_at: datetime
    :param trigger_date: The timestamp of the data that triggered the alert
     activity (for instance, if the alert activity
     was triggered by analysis of a flight, the flight date could be considered
     the trigger date)
    :type trigger_date: datetime
    :param is_active: Specifies whether the alert is Active or Inactive.
    :type is_active: bool
    :param state_changed: Specifies whether the alert state changed from the
     previous activity to this activity.
    :type state_changed: bool
    :param sort_key: A sortable string which orders the alert activity in
     ascending real-world chronological order.
    :type sort_key: str
    :param trigger_agent: Free-form string that identifies the agent which
     recorded the activity, such as a profile number.
    :type trigger_agent: str
    :param trigger_reference_type: Optional: caller-defined information which
     identifies what type of information
     is stored in TriggerReferenceValue. When returned from a call to set an
     alert's
     state, this is the value provided to that call. When returned from a call
     to get
     an alert's state, this is the value from the last time the alert actually
     changed
     state (from Active to Inactive or vice versa).
    :type trigger_reference_type: str
    :param trigger_reference_value: Optional: a record number or other value
     which was associated with this alert
     state change. For example, this may be the record number of a flight whose
     data was the cause of the state change (maybe through an APM alert
     trigger).
     When returned from a call to set an alert's state, this is the value
     provided to
     that call. When returned from a call to get an alert's state, this is the
     value
     from the last time the alert actually changed state (from Active to
     Inactive or
     vice versa).
    :type trigger_reference_value: int
    """

    _attribute_map = {
        'recorded_at': {'key': 'recordedAt', 'type': 'iso-8601'},
        'trigger_date': {'key': 'triggerDate', 'type': 'iso-8601'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'state_changed': {'key': 'stateChanged', 'type': 'bool'},
        'sort_key': {'key': 'sortKey', 'type': 'str'},
        'trigger_agent': {'key': 'triggerAgent', 'type': 'str'},
        'trigger_reference_type': {'key': 'triggerReferenceType', 'type': 'str'},
        'trigger_reference_value': {'key': 'triggerReferenceValue', 'type': 'int'},
    }

    def __init__(self, *, recorded_at=None, trigger_date=None, is_active: bool=None, state_changed: bool=None, sort_key: str=None, trigger_agent: str=None, trigger_reference_type: str=None, trigger_reference_value: int=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoAlertGetActivity, self).__init__(**kwargs)
        self.recorded_at = recorded_at
        self.trigger_date = trigger_date
        self.is_active = is_active
        self.state_changed = state_changed
        self.sort_key = sort_key
        self.trigger_agent = trigger_agent
        self.trigger_reference_type = trigger_reference_type
        self.trigger_reference_value = trigger_reference_value
