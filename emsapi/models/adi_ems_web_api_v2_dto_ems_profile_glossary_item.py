# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoEmsProfileGlossaryItem(Model):
    """Represents a single entry for an item in a profile glossary.

    :param record_type: A character representing a profile glossary entries
     record type.
    :type record_type: str
    :param scope: A character representing the scope of this entry.
    :type scope: str
    :param item_id: A unique integer id for this item.
    :type item_id: int
    :param event_type_id: The event type id of this item. This is only
     available for valid event types.
    :type event_type_id: int
    :param data_type: A character representing the data type of this entry.
    :type data_type: str
    :param logical_id: A GUID defining this item's logical id.
    :type logical_id: str
    :param name: The name provided for this item.
    :type name: str
    :param units: An optional unit provided for this item.
    :type units: str
    :param first_associated_item_type: The item type of the first associated
     item.
    :type first_associated_item_type: str
    :param first_associated_item_scope: The scope of the first associated
     item.
    :type first_associated_item_scope: str
    :param first_associated_item_id: The item id of the first associated item.
    :type first_associated_item_id: int
    :param second_associated_item_type: The item type of the second associated
     item.
    :type second_associated_item_type: str
    :param second_associated_item_scope: The scope of the second associated
     item.
    :type second_associated_item_scope: str
    :param second_associated_item_id: The item id of the second associated
     item.
    :type second_associated_item_id: int
    """

    _attribute_map = {
        'record_type': {'key': 'recordType', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'item_id': {'key': 'itemId', 'type': 'int'},
        'event_type_id': {'key': 'eventTypeId', 'type': 'int'},
        'data_type': {'key': 'dataType', 'type': 'str'},
        'logical_id': {'key': 'logicalId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'units': {'key': 'units', 'type': 'str'},
        'first_associated_item_type': {'key': 'firstAssociatedItemType', 'type': 'str'},
        'first_associated_item_scope': {'key': 'firstAssociatedItemScope', 'type': 'str'},
        'first_associated_item_id': {'key': 'firstAssociatedItemId', 'type': 'int'},
        'second_associated_item_type': {'key': 'secondAssociatedItemType', 'type': 'str'},
        'second_associated_item_scope': {'key': 'secondAssociatedItemScope', 'type': 'str'},
        'second_associated_item_id': {'key': 'secondAssociatedItemId', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoEmsProfileGlossaryItem, self).__init__(**kwargs)
        self.record_type = kwargs.get('record_type', None)
        self.scope = kwargs.get('scope', None)
        self.item_id = kwargs.get('item_id', None)
        self.event_type_id = kwargs.get('event_type_id', None)
        self.data_type = kwargs.get('data_type', None)
        self.logical_id = kwargs.get('logical_id', None)
        self.name = kwargs.get('name', None)
        self.units = kwargs.get('units', None)
        self.first_associated_item_type = kwargs.get('first_associated_item_type', None)
        self.first_associated_item_scope = kwargs.get('first_associated_item_scope', None)
        self.first_associated_item_id = kwargs.get('first_associated_item_id', None)
        self.second_associated_item_type = kwargs.get('second_associated_item_type', None)
        self.second_associated_item_scope = kwargs.get('second_associated_item_scope', None)
        self.second_associated_item_id = kwargs.get('second_associated_item_id', None)
