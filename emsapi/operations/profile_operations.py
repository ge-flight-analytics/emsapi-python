# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class ProfileOperations(object):
    """ProfileOperations operations.

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

    def get_profile_results(
            self, ems_system_id, flight_id, profile_id, custom_headers=None, raw=False, **operation_config):
        """Queries profile results for a specified flight and profile.

        <p>This API allows retrieving all of the timepoints, measurements, and
        events calculated for a
        specific flight with the configured profile.</p>
        <p>Use this API in conjunction with
        "ems-systems/{emsSystemId}/flights/{flightId}/profiles/{profileId}/glossary"
        API so you can interpret and
        better understand the results returned in the results.</p>.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param flight_id: The integer ID of the flight record to use when
         retrieving profile information.
        :type flight_id: int
        :param profile_id: The unique identifier of the APM profile, e.g.
         "A7483C44-9DB9-4A44-9EB5-F67681EE52B0" for
         the library flight safety events profile.
        :type profile_id: str
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
        url = self.get_profile_results.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'flightId': self._serialize.url("flight_id", flight_id, 'int'),
            'profileId': self._serialize.url("profile_id", profile_id, 'str')
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
            deserialized = self._deserialize('AdiEmsWebApiV2DtoProfileProfileResults', response)
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
    get_profile_results.metadata = {'url': '/v2/ems-systems/{emsSystemId}/flights/{flightId}/profiles/{profileId}/query'}

    def get_profile_group(
            self, ems_system_id, group_id=None, custom_headers=None, raw=False, **operation_config):
        """Returns a profile group with a matching ID containing only its
        immediate children in a hierarchical tree
        used to organize profiles.

        Each EMS system has its own configured set of profiles that are
        available. Profiles are organized using
        profile groups in a tree structure since EMS systems might expose a
        large number of profiles. This API
        allows you to see one level of the tree structure.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param group_id: The unique identifier of the profile group whose
         contents to return. If not
         specified, the contents of the root group are returned.
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
        url = self.get_profile_group.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if group_id is not None:
            query_parameters['groupId'] = self._serialize.query("group_id", group_id, 'str')

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
            deserialized = self._deserialize('AdiEmsWebApiV2DtoProfileProfileGroup', response)
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
    get_profile_group.metadata = {'url': '/v2/ems-systems/{emsSystemId}/profile-groups'}

    def get_profiles(
            self, ems_system_id, group_id=None, search=None, custom_headers=None, raw=False, **operation_config):
        """Returns all the profiles matching the specified search options.

        <p>
        This API will return profiles matching your search options. If no
        profiles are found, an empty list is
        returned.
        </p>
        <p>
        It is common for a large number of profiles to be defined on an EMS
        system. To reduce the size and complexity
        of your query, try to specify a parent profile group ID and/or a name
        to use in the search.
        </p>.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param group_id: The optional parent profile group ID whose contents
         to search.
        :type group_id: str
        :param search: An optional profile name search string used to match
         profiles to return.
        :type search: str
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
        url = self.get_profiles.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if group_id is not None:
            query_parameters['groupId'] = self._serialize.query("group_id", group_id, 'str')
        if search is not None:
            query_parameters['search'] = self._serialize.query("search", search, 'str')

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
            deserialized = self._deserialize('[AdiEmsWebApiV2DtoProfileProfile]', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_profiles.metadata = {'url': '/v2/ems-systems/{emsSystemId}/profiles'}

    def get_profile_glossary(
            self, ems_system_id, profile_id, profile_version=None, format=None, custom_headers=None, raw=False, **operation_config):
        """Returns a "glossary" for a specific profile and version, which helps
        define the results that can be returned
        in a profile.

        <p>
        <strong>Please note:</strong> this API is prototypical in this release
        and its return values are subject
        to change in an upcoming release. In its current implementation, it is
        (1) including some unnecessary
        results and (2) not returning all available information.</p>
        <p>Use this API in conjunction with
        "ems-systems/{emsSystemId}/flights/{flightId}/profiles/{profileId}/query"
        API so you can interpret and
        better understand the results returned in the results.</p>.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param profile_id: The unique identifier of the profile whose glossary
         to return, e.g.
         "A7483C44-9DB9-4A44-9EB5-F67681EE52B0".
        :type profile_id: str
        :param profile_version: Integer version of the profile to return. If
         not specified the current version
         of the profile is used by default.
        :type profile_version: int
        :param format: The format of the returned glossary. Defaults to JSON.
         Possible values include: 'json', 'csv'
        :type format: str
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
        url = self.get_profile_glossary.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'profileId': self._serialize.url("profile_id", profile_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if profile_version is not None:
            query_parameters['profileVersion'] = self._serialize.query("profile_version", profile_version, 'int')
        if format is not None:
            query_parameters['format'] = self._serialize.query("format", format, 'str')

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
            deserialized = self._deserialize('AdiEmsWebApiV2DtoProfileProfileGlossary', response)
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
    get_profile_glossary.metadata = {'url': '/v2/ems-systems/{emsSystemId}/profiles/{profileId}/glossary'}

    def get_profile_events(
            self, ems_system_id, profile_id, custom_headers=None, raw=False, **operation_config):
        """Returns the events for a specific profile.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param profile_id: The unique identifier of the profile whose events
         to return, e.g.
         "A7483C44-9DB9-4A44-9EB5-F67681EE52B0".
        :type profile_id: str
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
        url = self.get_profile_events.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'profileId': self._serialize.url("profile_id", profile_id, 'str')
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
            deserialized = self._deserialize('[AdiEmsWebApiV2DtoProfileEvent]', response)
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
    get_profile_events.metadata = {'url': '/v2/ems-systems/{emsSystemId}/profiles/{profileId}/events'}

    def get_event_parameter_set(
            self, ems_system_id, profile_id, event_id, custom_headers=None, raw=False, **operation_config):
        """Returns an event for a specific profile.

        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param profile_id: The unique identifier of the profile whose event
         parameter set is returned, e.g.
         "A7483C44-9DB9-4A44-9EB5-F67681EE52B0".
        :type profile_id: str
        :param event_id: The integer ID for the event.
        :type event_id: int
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
        url = self.get_event_parameter_set.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'profileId': self._serialize.url("profile_id", profile_id, 'str'),
            'eventId': self._serialize.url("event_id", event_id, 'int')
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
            deserialized = self._deserialize('AdiEmsWebApiV2DtoProfileEvent', response)
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
    get_event_parameter_set.metadata = {'url': '/v2/ems-systems/{emsSystemId}/profiles/{profileId}/events/{eventId}'}
