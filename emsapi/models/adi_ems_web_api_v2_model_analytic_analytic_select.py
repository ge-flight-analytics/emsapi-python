# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2ModelAnalyticAnalyticSelect(Model):
    """Represents an individual analytic that can be selected in a query.

    All required parameters must be populated in order to send to Azure.

    :param analytic_id: Required. The unique string identifier of the analytic
     to select in a query
    :type analytic_id: str
    """

    _validation = {
        'analytic_id': {'required': True},
    }

    _attribute_map = {
        'analytic_id': {'key': 'analyticId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2ModelAnalyticAnalyticSelect, self).__init__(**kwargs)
        self.analytic_id = kwargs.get('analytic_id', None)
