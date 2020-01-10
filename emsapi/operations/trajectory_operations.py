# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class TrajectoryOperations(object):
    """TrajectoryOperations operations.

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

    def get_kml_for_flight(
            self, ems_system_id, flight_id, trajectory_id, custom_headers=None, raw=False, **operation_config):
        """Returns trajectory content in "KML" format for a specific flight.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param flight_id: The integer ID of the flight record to use when
         retrieving the trajectory KML.
        :type flight_id: int
        :param trajectory_id: Identifier specifying the type of trajectory to
         provide.
        :type trajectory_id: str
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
        url = self.get_kml_for_flight.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'flightId': self._serialize.url("flight_id", flight_id, 'int'),
            'trajectoryId': self._serialize.url("trajectory_id", trajectory_id, 'str')
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
            deserialized = self._deserialize('object', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_kml_for_flight.metadata = {'url': '/v2/ems-systems/{emsSystemId}/flights/{flightId}/kml-trajectories/{trajectoryId}'}

    def generate_trajectory_for_flight(
            self, ems_system_id, flight_id, start=None, end=None, custom_headers=None, raw=False, **operation_config):
        """Returns a trajectory path for a specific flight.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param flight_id: The integer ID of the flight record to use when
         retrieving the trajectory data.
        :type flight_id: int
        :param start: The start offset in the data, in seconds from the start
         of the data. If not specified, the beginning of the flight will be
         used.
        :type start: float
        :param end: The end offset in the data, in seconds from the start of
         the data. If not specified, the end of the flight will be used.
        :type end: float
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
        url = self.generate_trajectory_for_flight.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'flightId': self._serialize.url("flight_id", flight_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'float')
        if end is not None:
            query_parameters['end'] = self._serialize.query("end", end, 'float')

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
            deserialized = self._deserialize('AdiEmsWebApiV2DtoTrajectoryValueArray', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    generate_trajectory_for_flight.metadata = {'url': '/v2/ems-systems/{emsSystemId}/flights/{flightId}/trajectories'}

    def get_trajectory_configurations(
            self, ems_system_id, custom_headers=None, raw=False, **operation_config):
        """Returns an array of KML trajectory options.

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
        url = self.get_trajectory_configurations.metadata['url']
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
            deserialized = self._deserialize('[AdiEmsWebApiV2DtoTrajectoryConfiguration]', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_trajectory_configurations.metadata = {'url': '/v2/ems-systems/{emsSystemId}/trajectory-configurations'}
