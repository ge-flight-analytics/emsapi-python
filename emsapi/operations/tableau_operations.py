# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class TableauOperations(object):
    """TableauOperations operations.

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

    def get_trusted(
            self, site=None, custom_headers=None, raw=False, **operation_config):
        """Returns a Tableau "trusted" URL that consumers can use to gain access
        to Tableau content.

        <p>The returned "trusted" URL allows consumers connect to Tableau using
        the current user's security
        context. Once loaded in an iframe of a browser, Tableau sets a cookie
        to initiate the user's session.</p>.

        :param site: The name of the Tableau site for which to return a
         trusted URL. If not specified, the
         default site is used.
        :type site: str
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
        url = self.get_trusted.metadata['url']

        # Construct parameters
        query_parameters = {}
        if site is not None:
            query_parameters['site'] = self._serialize.query("site", site, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 404, 500, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2ModelTableauTrusted', response)
        if response.status_code == 400:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 500:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_trusted.metadata = {'url': '/v2/tableau/trusted'}

    def get_tableau(
            self, site=None, custom_headers=None, raw=False, **operation_config):
        """Returns information about the configured EMS Online Tableau server.

        <p>The return is information about the Tableau server configured in EMS
        Online.</p>.

        :param site: The name of the Tableau site for which to return Tableau
         server information. If not specified, the default site is used.
        :type site: str
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
        url = self.get_tableau.metadata['url']

        # Construct parameters
        query_parameters = {}
        if site is not None:
            query_parameters['site'] = self._serialize.query("site", site, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 404, 500, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2ModelTableauTableauServer', response)
        if response.status_code == 400:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 500:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_tableau.metadata = {'url': '/v2/tableau'}

    def get_sites(
            self, custom_headers=None, raw=False, **operation_config):
        """Returns the Tableau sites containing projects, workbooks and views the
        user can access.

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
        url = self.get_sites.metadata['url']

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

        if response.status_code not in [200, 401, 404, 500, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[AdiEmsWebSharedTableauRestSite]', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 500:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_sites.metadata = {'url': '/v2/tableau/sites'}

    def get_site_projects(
            self, site_id, custom_headers=None, raw=False, **operation_config):
        """Returns the Tableau projects in the specified site, containing
        workbooks and views the user can access.

        :param site_id: The ID of the site containing the projects to return.
        :type site_id: str
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
        url = self.get_site_projects.metadata['url']
        path_format_arguments = {
            'siteId': self._serialize.url("site_id", site_id, 'str')
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

        if response.status_code not in [200, 401, 404, 500, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[AdiEmsWebSharedTableauRestProject]', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 500:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_site_projects.metadata = {'url': '/v2/tableau/sites/{siteId}/projects'}

    def get_site_workbooks(
            self, site_id, custom_headers=None, raw=False, **operation_config):
        """Returns the Tableau workbooks in the specified site, containing views
        the user can access.

        :param site_id: The ID of the site containing the workbooks to return.
        :type site_id: str
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
        url = self.get_site_workbooks.metadata['url']
        path_format_arguments = {
            'siteId': self._serialize.url("site_id", site_id, 'str')
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

        if response.status_code not in [200, 401, 404, 500, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[AdiEmsWebSharedTableauRestWorkbook]', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 500:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_site_workbooks.metadata = {'url': '/v2/tableau/sites/{siteId}/workbooks'}

    def get_site_workbook_views(
            self, site_id, workbook_id, custom_headers=None, raw=False, **operation_config):
        """Returns the Tableau views in the specified site and workbook,
        containing content the user can visualize.

        :param site_id: The ID of the site containing the view.
        :type site_id: str
        :param workbook_id: The ID of the workbook containing the view.
        :type workbook_id: str
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
        url = self.get_site_workbook_views.metadata['url']
        path_format_arguments = {
            'siteId': self._serialize.url("site_id", site_id, 'str'),
            'workbookId': self._serialize.url("workbook_id", workbook_id, 'str')
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

        if response.status_code not in [200, 401, 404, 500, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[AdiEmsWebSharedTableauRestView]', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 500:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_site_workbook_views.metadata = {'url': '/v2/tableau/sites/{siteId}/workbooks/{workbookId}/views'}