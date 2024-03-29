# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAnalyticFormula(Model):
    """Encapsulates the information needed to create a new analytic formula.

    All required parameters must be populated in order to send to Azure.

    :param name: The name of the new analytic formula, if any
    :type name: str
    :param description: The description of the new analytic formula, if any
    :type description: str
    :param units: The units for the new analytic formula, if any
    :type units: str
    :param body: Required. The formula body text for the new analytic. If this
     formula references other analytics, they should
     be inserted into the formula by name between square brackets, e.g.
     "[MyAnalytic]"
    :type body: str
    :param used_analytics: The other analytics that are referenced by the
     formula. The name property of these analytics
     should match the names used in the formula text between square brackets
    :type used_analytics: list[~emsapi.models.AdiEmsWebApiV2DtoUsedAnalytic]
    :param used_analytic_name_for_metadata: The name of one of the
     UsedAnalytics (if any) that will be used as the source of metadata for
     this new formula
    :type used_analytic_name_for_metadata: str
    """

    _validation = {
        'body': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'units': {'key': 'units', 'type': 'str'},
        'body': {'key': 'body', 'type': 'str'},
        'used_analytics': {'key': 'usedAnalytics', 'type': '[AdiEmsWebApiV2DtoUsedAnalytic]'},
        'used_analytic_name_for_metadata': {'key': 'usedAnalyticNameForMetadata', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoAnalyticFormula, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.units = kwargs.get('units', None)
        self.body = kwargs.get('body', None)
        self.used_analytics = kwargs.get('used_analytics', None)
        self.used_analytic_name_for_metadata = kwargs.get('used_analytic_name_for_metadata', None)
