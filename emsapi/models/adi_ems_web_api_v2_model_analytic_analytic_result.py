# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2ModelAnalyticAnalyticResult(Model):
    """Represents the results of a query of an individual analytic, housing the
    values for the offsets contained
    in the related query result.

    All required parameters must be populated in order to send to Azure.

    :param analytic_id: Required. The unique string identifier of the analytic
     queried
    :type analytic_id: str
    :param alias: The (optional) custom name of the analytic that produced
     these results
    :type alias: str
    :param values: Required. The array of analytic values corresponding to
     offsets specified in the query result
    :type values: list[object]
    :param error: Any error that may have occurred when retrieving or
     attempting to retrieve the values for the analytic.
     This field is only available if there is an error.
    :type error: str
    """

    _validation = {
        'analytic_id': {'required': True},
        'values': {'required': True},
    }

    _attribute_map = {
        'analytic_id': {'key': 'analyticId', 'type': 'str'},
        'alias': {'key': 'alias', 'type': 'str'},
        'values': {'key': 'values', 'type': '[object]'},
        'error': {'key': 'error', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2ModelAnalyticAnalyticResult, self).__init__(**kwargs)
        self.analytic_id = kwargs.get('analytic_id', None)
        self.alias = kwargs.get('alias', None)
        self.values = kwargs.get('values', None)
        self.error = kwargs.get('error', None)
