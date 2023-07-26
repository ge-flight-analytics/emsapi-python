# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaNewComment(Model):
    """The model representing a new comment to be added.

    All required parameters must be populated in order to send to Azure.

    :param comment: Required. The comment text to be added
    :type comment: str
    :param entity_identifier: Required. The unique identifier of the entity
     (flight, event, etc.) that the comment is associated with.
     This is an array since some entity types have compound primary keys
     (multiple fields).
     These should be primary key values on the entity's database and should be
     in order. These should
     uniquely identify a single entity
    :type entity_identifier: list[object]
    """

    _validation = {
        'comment': {'required': True},
        'entity_identifier': {'required': True},
    }

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'entity_identifier': {'key': 'entityIdentifier', 'type': '[object]'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoSchemaNewComment, self).__init__(**kwargs)
        self.comment = kwargs.get('comment', None)
        self.entity_identifier = kwargs.get('entity_identifier', None)
