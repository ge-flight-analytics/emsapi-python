# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAnalyticSetNewAnalyticSetItem(Model):
    """A model that encapsulates the data for a single analytic in an analytic
    set.

    :param chart_index: The index of the chart that this analytic info belongs
     to, or null if no index specified
    :type chart_index: int
    :param chart_size: The size of the chart or null if not specified.
     Possible values: [Normal, Small]
    :type chart_size: str
    :param analytic_id: The analytic identifier that is represented by this
     analytic set item
    :type analytic_id: str
    :param custom_name: The custom name the user specified for the item, or
     null if not-specified
    :type custom_name: str
    :param color: The color to use for the line in hexadecimal color
     specification "#RRGGBB", or null if no color specified
    :type color: str
    :param custom_range: Optional override for the vertical scale for an
     analytic
    :type custom_range: ~emsapi.models.AdiEmsWebApiCoreDtoDataRange
    :param custom_digits_after_decimal: Optional override for the number of
     digits to display
    :type custom_digits_after_decimal: int
    :param line_width: Optional value from 1 to 5 for the width of the line
    :type line_width: int
    :param display_sample_marker: Optional value specifying whether the
     parameter should display shapes to indicate the sampled values
    :type display_sample_marker: bool
    :param sample_marker_shape: If set, describes the shape to use for the
     sampled values.
     Possible values: [Square, Circle, Triangle, InvertedTriangle, Cross, Star]
    :type sample_marker_shape: str
    :param line_style: If set, describes the line style to use when drawing.
     Possible values: [Dash, Dot, DashDot, DashDotDot, Solid]
    :type line_style: str
    :param parameter_filtering_mode: Whether parameter filtering mode should
     be enabled for this item or not.
     possible values: [Default, Enabled, Disabled]
    :type parameter_filtering_mode: str
    :param interpolation_mode: The way in which the data should be
     interpolated.
     Possible values: [Default, StairStep, Continuous].
    :type interpolation_mode: str
    """

    _attribute_map = {
        'chart_index': {'key': 'chartIndex', 'type': 'int'},
        'chart_size': {'key': 'chartSize', 'type': 'str'},
        'analytic_id': {'key': 'analyticId', 'type': 'str'},
        'custom_name': {'key': 'customName', 'type': 'str'},
        'color': {'key': 'color', 'type': 'str'},
        'custom_range': {'key': 'customRange', 'type': 'AdiEmsWebApiCoreDtoDataRange'},
        'custom_digits_after_decimal': {'key': 'customDigitsAfterDecimal', 'type': 'int'},
        'line_width': {'key': 'lineWidth', 'type': 'int'},
        'display_sample_marker': {'key': 'displaySampleMarker', 'type': 'bool'},
        'sample_marker_shape': {'key': 'sampleMarkerShape', 'type': 'str'},
        'line_style': {'key': 'lineStyle', 'type': 'str'},
        'parameter_filtering_mode': {'key': 'parameterFilteringMode', 'type': 'str'},
        'interpolation_mode': {'key': 'interpolationMode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoAnalyticSetNewAnalyticSetItem, self).__init__(**kwargs)
        self.chart_index = kwargs.get('chart_index', None)
        self.chart_size = kwargs.get('chart_size', None)
        self.analytic_id = kwargs.get('analytic_id', None)
        self.custom_name = kwargs.get('custom_name', None)
        self.color = kwargs.get('color', None)
        self.custom_range = kwargs.get('custom_range', None)
        self.custom_digits_after_decimal = kwargs.get('custom_digits_after_decimal', None)
        self.line_width = kwargs.get('line_width', None)
        self.display_sample_marker = kwargs.get('display_sample_marker', None)
        self.sample_marker_shape = kwargs.get('sample_marker_shape', None)
        self.line_style = kwargs.get('line_style', None)
        self.parameter_filtering_mode = kwargs.get('parameter_filtering_mode', None)
        self.interpolation_mode = kwargs.get('interpolation_mode', None)
