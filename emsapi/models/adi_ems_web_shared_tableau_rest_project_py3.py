# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebSharedTableauRestProject(Model):
    """AdiEmsWebSharedTableauRestProject.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param description:
    :type description: str
    :param content_permissions:
    :type content_permissions: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'content_permissions': {'key': 'contentPermissions', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, description: str=None, content_permissions: str=None, **kwargs) -> None:
        super(AdiEmsWebSharedTableauRestProject, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.description = description
        self.content_permissions = content_permissions
