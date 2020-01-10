# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebSharedTableauRestView(Model):
    """AdiEmsWebSharedTableauRestView.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param content_url:
    :type content_url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, content_url: str=None, **kwargs) -> None:
        super(AdiEmsWebSharedTableauRestView, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.content_url = content_url
