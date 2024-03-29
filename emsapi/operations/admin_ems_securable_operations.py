# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class AdminEmsSecurableOperations(object):
    """AdminEmsSecurableOperations operations.

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

    def get_user_access_for_securable(
            self, ems_system_id, securable_id, access_right, username, custom_headers=None, raw=False, **operation_config):
        """Returns the effective access permission for the given securable and
        access right for a given user.

        :param ems_system_id: The unique identifier of the system containing
         the EMS securable.
        :type ems_system_id: int
        :param securable_id: The ID of the securable to check access for.
        :type securable_id: str
        :param access_right: The name of the access right for the securable.
         This has to be a valid access right for the specific type of
         securable.
        :type access_right: str
        :param username: The username of the user to check the securable
         access right against.
        :type username: str
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
        url = self.get_user_access_for_securable.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'securableId': self._serialize.url("securable_id", securable_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['accessRight'] = self._serialize.query("access_right", access_right, 'str')
        query_parameters['username'] = self._serialize.query("username", username, 'str')

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
            deserialized = self._deserialize('AdiEmsWebApiV2DtoEmsSecurableEmsSecurableEffectiveAccess', response)
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
    get_user_access_for_securable.metadata = {'url': '/v2/admin/ems-systems/{emsSystemId}/securables/{securableId}'}
