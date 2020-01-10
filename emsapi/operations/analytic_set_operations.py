# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class AnalyticSetOperations(object):
    """AnalyticSetOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_analytic_set_groups(
            self, ems_system_id, custom_headers=None, raw=False, **operation_config):
        """Returns a collection of analytic set groups.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_analytic_set_groups.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 401, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoAnalyticSetAnalyticSetGroup', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_analytic_set_groups.metadata = {'url': '/v2/ems-systems/{emsSystemId}/analytic-set-groups'}

    def get_analytic_set_group(
            self, ems_system_id, group_id, custom_headers=None, raw=False, **operation_config):
        """Returns an analytic set group.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param group_id: The ID of the analytic set group to return.
        :type group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_analytic_set_group.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'groupId': self._serialize.url("group_id", group_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 401, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoAnalyticSetAnalyticSetGroup', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_analytic_set_group.metadata = {'url': '/v2/ems-systems/{emsSystemId}/analytic-set-groups/{groupId}'}

    def get_parameter_sets(
            self, ems_system_id, group_id, analytic_set_name, custom_headers=None, raw=False, **operation_config):
        """Returns an analytic set with the provided name from the group
        requested.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param group_id: The ID of the analytic set group to retrieve the
         analytic set from.
        :type group_id: str
        :param analytic_set_name: The name of the analytic set to return.
        :type analytic_set_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_parameter_sets.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'groupId': self._serialize.url("group_id", group_id, 'str'),
            'analyticSetName': self._serialize.url("analytic_set_name", analytic_set_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 401, 404, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoAnalyticSetAnalyticSet', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_parameter_sets.metadata = {'url': '/v2/ems-systems/{emsSystemId}/analytic-set-groups/{groupId}/analytic-sets/{analyticSetName}'}
