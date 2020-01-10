# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebSharedTableauRestWorkbook(Model):
    """AdiEmsWebSharedTableauRestWorkbook.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param content_url:
    :type content_url: str
    :param show_tabs:
    :type show_tabs: bool
    :param size:
    :type size: int
    :param created_at:
    :type created_at: datetime
    :param updated_at:
    :type updated_at: datetime
    :param project:
    :type project: ~emsapi.models.AdiEmsWebSharedTableauRestProject
    :param owner:
    :type owner: ~emsapi.models.AdiEmsWebSharedTableauRestUser
    :param tags:
    :type tags: ~emsapi.models.AdiEmsWebSharedTableauRestTags
    :param views:
    :type views: ~emsapi.models.AdiEmsWebSharedTableauRestViews
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'show_tabs': {'key': 'showTabs', 'type': 'bool'},
        'size': {'key': 'size', 'type': 'int'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'updatedAt', 'type': 'iso-8601'},
        'project': {'key': 'project', 'type': 'AdiEmsWebSharedTableauRestProject'},
        'owner': {'key': 'owner', 'type': 'AdiEmsWebSharedTableauRestUser'},
        'tags': {'key': 'tags', 'type': 'AdiEmsWebSharedTableauRestTags'},
        'views': {'key': 'views', 'type': 'AdiEmsWebSharedTableauRestViews'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebSharedTableauRestWorkbook, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.content_url = kwargs.get('content_url', None)
        self.show_tabs = kwargs.get('show_tabs', None)
        self.size = kwargs.get('size', None)
        self.created_at = kwargs.get('created_at', None)
        self.updated_at = kwargs.get('updated_at', None)
        self.project = kwargs.get('project', None)
        self.owner = kwargs.get('owner', None)
        self.tags = kwargs.get('tags', None)
        self.views = kwargs.get('views', None)
