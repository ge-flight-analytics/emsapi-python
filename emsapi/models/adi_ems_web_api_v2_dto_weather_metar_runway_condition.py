# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherMetarRunwayCondition(Model):
    """Describes the condition of a runway.

    All required parameters must be populated in order to send to Azure.

    :param unparsed: Required. The original, unparsed runway conditions string
    :type unparsed: str
    :param runway: Required. The name/number/approach direction identifying
     the runway
    :type runway: str
    :param deposit_type: The type of deposits currently on the runway.
     Possible values include: 'dry', 'damp', 'wet', 'frost', 'snowDry',
     'snowWet', 'slush', 'ice', 'snowCompacted', 'frozenRuts', 'none'
    :type deposit_type: str or ~emsapi.models.enum
    :param coverage: The coverage of deposits currently on the runway.
     Possible values include: 'coverage10Less', 'coverage11To25',
     'covarege26To50', 'coverage51To100', 'noInformation'
    :type coverage: str or ~emsapi.models.enum
    :param depth: Indicates the depth of deposits currently on the runway in
     centimeters
    :type depth: float
    :param braking: The "braking action" value describing the current braking
     conditions of the runway. Possible values include: 'unreliable', 'poor',
     'mediumPoor', 'medium', 'mediumGood', 'good', 'none'
    :type braking: str or ~emsapi.models.enum
    :param friction: The "coefficient of friction" value that alternatively
     describes the current braking conditions of the
     runway
    :type friction: float
    :param is_clear: Required. Indicating whether the runway conditions are
     clear of deposits
    :type is_clear: bool
    """

    _validation = {
        'unparsed': {'required': True},
        'runway': {'required': True},
        'is_clear': {'required': True},
    }

    _attribute_map = {
        'unparsed': {'key': 'unparsed', 'type': 'str'},
        'runway': {'key': 'runway', 'type': 'str'},
        'deposit_type': {'key': 'depositType', 'type': 'str'},
        'coverage': {'key': 'coverage', 'type': 'str'},
        'depth': {'key': 'depth', 'type': 'float'},
        'braking': {'key': 'braking', 'type': 'str'},
        'friction': {'key': 'friction', 'type': 'float'},
        'is_clear': {'key': 'isClear', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoWeatherMetarRunwayCondition, self).__init__(**kwargs)
        self.unparsed = kwargs.get('unparsed', None)
        self.runway = kwargs.get('runway', None)
        self.deposit_type = kwargs.get('deposit_type', None)
        self.coverage = kwargs.get('coverage', None)
        self.depth = kwargs.get('depth', None)
        self.braking = kwargs.get('braking', None)
        self.friction = kwargs.get('friction', None)
        self.is_clear = kwargs.get('is_clear', None)
