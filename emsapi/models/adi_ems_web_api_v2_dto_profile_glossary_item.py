# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoProfileGlossaryItem(Model):
    """Represents a single entry for an item in a profile glossary.

    All required parameters must be populated in order to send to Azure.

    :param record_type: Required. A value representing a profile glossary
     entries record type. Possible values include: 'measurement', 'timepoint',
     'event', 'interval'
    :type record_type: str or ~emsapi.models.enum
    :param scope: Required. A value representing the scope of the item.
     Possible values include: 'default', 'eventSpecific', 'eventGlobal'
    :type scope: str or ~emsapi.models.enum
    :param item_id: Required. A unique integer ID for the item
    :type item_id: int
    :param event_type_id: The event type ID of the item - this is only
     available for valid event types
    :type event_type_id: int
    :param data_type: A value representing the data type of the entry.
     Possible values include: 'floatingPoint'
    :type data_type: str or ~emsapi.models.enum
    :param logical_id: Required. A unique ID defining the item's logical ID
    :type logical_id: str
    :param name: Required. The display name of the item
    :type name: str
    :param units: An optional unit describing how the type of data represented
     by the item
    :type units: str
    :param first_associated_item_type: The item type of the first associated
     item. Possible values include: 'measurement', 'timepoint', 'event',
     'interval'
    :type first_associated_item_type: str or ~emsapi.models.enum
    :param first_associated_item_scope: The scope of the first associated
     item. Possible values include: 'default', 'eventSpecific', 'eventGlobal'
    :type first_associated_item_scope: str or ~emsapi.models.enum
    :param first_associated_item_id: The item id of the first associated item
    :type first_associated_item_id: int
    :param second_associated_item_type: The item type of the second associated
     item. Possible values include: 'measurement', 'timepoint', 'event',
     'interval'
    :type second_associated_item_type: str or ~emsapi.models.enum
    :param second_associated_item_scope: The scope of the second associated
     item. Possible values include: 'default', 'eventSpecific', 'eventGlobal'
    :type second_associated_item_scope: str or ~emsapi.models.enum
    :param second_associated_item_id: The item id of the second associated
     item
    :type second_associated_item_id: int
    :param is_saved_to_database: A flag describing if a measurement is saved
     to the database
    :type is_saved_to_database: bool
    :param comments: The comments on the object.
    :type comments: str
    :param properties: Additional metadata on the object.
    :type properties: ~emsapi.models.AdiEmsWebApiV2DtoMetadata
    """

    _validation = {
        'record_type': {'required': True},
        'scope': {'required': True},
        'item_id': {'required': True},
        'logical_id': {'required': True},
        'name': {'required': True},
    }

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
        'is_saved_to_database': {'key': 'isSavedToDatabase', 'type': 'bool'},
        'comments': {'key': 'comments', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'AdiEmsWebApiV2DtoMetadata'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoProfileGlossaryItem, self).__init__(**kwargs)
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
        self.is_saved_to_database = kwargs.get('is_saved_to_database', None)
        self.comments = kwargs.get('comments', None)
        self.properties = kwargs.get('properties', None)
