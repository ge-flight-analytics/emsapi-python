# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaFilter(Model):
    """Represents the operations and arguments that can be used to filter a data
    source query.

    All required parameters must be populated in order to send to Azure.

    :param operator: Required. The unique string identifier of the operation
     to perform. Possible values include: 'isTrue', 'isFalse', 'isNull',
     'isNotNull', 'and', 'or', 'not', 'in', 'notIn', 'plus', 'minus',
     'multiply', 'divide', 'modulo', 'equal', 'notEqual', 'lessThan',
     'lessThanOrEqual', 'greaterThan', 'greaterThanOrEqual',
     'betweenInclusive', 'betweenLowerExclusive', 'betweenUpperExclusive',
     'betweenExclusive', 'notBetweenInclusive', 'notBetweenLowerExclusive',
     'notBetweenUpperExclusive', 'notBetweenExclusive', 'integerRangeInclude',
     'integerRangeExclude', 'realRangeInclude', 'realRangeExclude', 'like',
     'notLike', 'allWords', 'anyWords', 'noWords', 'dateRelative',
     'dateSpecificMonths', 'dateSpecificMonth', 'dateBeforeMonth',
     'dateOnAfterMonth', 'dateSpecificDays', 'dateSpecificDay',
     'dateBeforeDay', 'dateOnAfterDay', 'dateTimeRange', 'dateTimeBefore',
     'dateTimeOnAfter', 'dateQuarterOfYear', 'dateMonthOfYear',
     'dateDayOfWeek', 'dateTimeHourOfDay'
    :type operator: str or ~emsapi.models.enum
    :param args: Required. An ordered list of arguments to provide the
     operator. The requirements for the arguments depend on which
     operation is being performed
    :type args: list[~emsapi.models.AdiEmsWebApiV2DtoSchemaFilterArgument]
    """

    _validation = {
        'operator': {'required': True},
        'args': {'required': True},
    }

    _attribute_map = {
        'operator': {'key': 'operator', 'type': 'str'},
        'args': {'key': 'args', 'type': '[AdiEmsWebApiV2DtoSchemaFilterArgument]'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoSchemaFilter, self).__init__(**kwargs)
        self.operator = kwargs.get('operator', None)
        self.args = kwargs.get('args', None)