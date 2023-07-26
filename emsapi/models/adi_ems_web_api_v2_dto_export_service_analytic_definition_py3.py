# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoExportServiceAnalyticDefinition(Model):
    """Represents the options used to make up an analytic export service.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The (display) name of the export service
    :type name: str
    :param description: An optional description for the export service
    :type description: str
    :param database_id: Required. The identifier of the database on which the
     anlytics are based.
    :type database_id: str
    :param export_type: Required. The type of export to produce (e.g.
     text-based CSV, Parquet, etc.). Possible values include: 'textCsv',
     'parquet'
    :type export_type: str or ~emsapi.models.enum
    :param select: Required. An array specifying the analytics (e.g.
     parameters) to be included in the export
     Use null or an empty array to return only offset values
    :type select:
     list[~emsapi.models.AdiEmsWebApiV2ModelAnalyticAnalyticSelect]
    :param offset_type: Required. This defines the way in which the offsets
     are determined
    :type offset_type: ~emsapi.models.AdiEmsWebApiV2ModelAnalyticOffsetType
    :param start: The optional analytic identifier representing the start
     offset in the data, in seconds from the start of the data.
     If not specified, the beginning of the available data is used
    :type start: ~emsapi.models.AdiEmsWebApiV2ModelAnalyticAnalyticId
    :param end: The optional analytic identifier representing the end offset
     in the data, in seconds from the start of the data.
     If not specified, the end of the available data is used
    :type end: ~emsapi.models.AdiEmsWebApiV2ModelAnalyticAnalyticId
    :param unsampled_data_mode: This determines how to treat data values for
     offsets that are not sampled. If left unset this defaults to 'leaveBlank'.
     This only applies when performing queries using an "OffsetType" other than
     sampled values. Possible values include: 'leaveBlank',
     'uniquePreviousSample', 'stairStep', 'linearInterpolation',
     'parameterDefault', 'previousSample'
    :type unsampled_data_mode: str or ~emsapi.models.enum
    :param unsampled_value: This optional parameter replaces any unsampled
     (blank) values with a constant value. This defaults to a null value.
     This only applies for TextCsv exports - specifically when performing
     exports using an "OffsetType" other than sampled values
    :type unsampled_value: str
    :param does_not_exist_value: This optional parameter replaces any values
     that come back as DNE (does not exist) with a constant value. This
     defaults to "DNE".
     This only applies for TextCsv exports - specifically when performing
     queries using an "OffsetType" other than sampled values
    :type does_not_exist_value: str
    :param filtering: The filtering used to narrow down the set of entities
     (e.g. flights) that should be exported
    :type filtering: ~emsapi.models.AdiEmsWebApiV2DtoSchemaFilter
    :param azure_blob_container: Required. The name of the Azure blob
     container where the export blob output will be written
     (see AzureBlobName property for the name of the blob).
     NOTE: This container must already exist in order for the export to
     complete successfully
    :type azure_blob_container: str
    :param azure_blob_path: Required. An analytic identifer that defines the
     path (relative to the blob container) of the export blob output
    :type azure_blob_path:
     ~emsapi.models.AdiEmsWebApiV2ModelAnalyticAnalyticId
    :param azure_blob_connection_string: Required. The connection string to
     the Azure blob store where the export output will be written
    :type azure_blob_connection_string: str
    """

    _validation = {
        'name': {'required': True},
        'database_id': {'required': True},
        'export_type': {'required': True},
        'select': {'required': True},
        'offset_type': {'required': True},
        'azure_blob_container': {'required': True},
        'azure_blob_path': {'required': True},
        'azure_blob_connection_string': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'database_id': {'key': 'databaseId', 'type': 'str'},
        'export_type': {'key': 'exportType', 'type': 'str'},
        'select': {'key': 'select', 'type': '[AdiEmsWebApiV2ModelAnalyticAnalyticSelect]'},
        'offset_type': {'key': 'offsetType', 'type': 'AdiEmsWebApiV2ModelAnalyticOffsetType'},
        'start': {'key': 'start', 'type': 'AdiEmsWebApiV2ModelAnalyticAnalyticId'},
        'end': {'key': 'end', 'type': 'AdiEmsWebApiV2ModelAnalyticAnalyticId'},
        'unsampled_data_mode': {'key': 'unsampledDataMode', 'type': 'str'},
        'unsampled_value': {'key': 'unsampledValue', 'type': 'str'},
        'does_not_exist_value': {'key': 'doesNotExistValue', 'type': 'str'},
        'filtering': {'key': 'filtering', 'type': 'AdiEmsWebApiV2DtoSchemaFilter'},
        'azure_blob_container': {'key': 'azureBlobContainer', 'type': 'str'},
        'azure_blob_path': {'key': 'azureBlobPath', 'type': 'AdiEmsWebApiV2ModelAnalyticAnalyticId'},
        'azure_blob_connection_string': {'key': 'azureBlobConnectionString', 'type': 'str'},
    }

    def __init__(self, *, name: str, database_id: str, export_type, select, offset_type, azure_blob_container: str, azure_blob_path, azure_blob_connection_string: str, description: str=None, start=None, end=None, unsampled_data_mode=None, unsampled_value: str=None, does_not_exist_value: str=None, filtering=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoExportServiceAnalyticDefinition, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.database_id = database_id
        self.export_type = export_type
        self.select = select
        self.offset_type = offset_type
        self.start = start
        self.end = end
        self.unsampled_data_mode = unsampled_data_mode
        self.unsampled_value = unsampled_value
        self.does_not_exist_value = does_not_exist_value
        self.filtering = filtering
        self.azure_blob_container = azure_blob_container
        self.azure_blob_path = azure_blob_path
        self.azure_blob_connection_string = azure_blob_connection_string
