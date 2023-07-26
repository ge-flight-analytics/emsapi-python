# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.exceptions import HttpOperationError
from .operations.admin_api_client_operations import AdminApiClientOperations
from .operations.admin_application_operations import AdminApplicationOperations
from .operations.admin_dashboard_operations import AdminDashboardOperations
from .operations.admin_ems_securable_operations import AdminEmsSecurableOperations
from .operations.admin_ems_system_operations import AdminEmsSystemOperations
from .operations.admin_group_operations import AdminGroupOperations
from .operations.admin_user_operations import AdminUserOperations
from .operations.alert_operations import AlertOperations
from .operations.analytic_operations import AnalyticOperations
from .operations.analytic_set_operations import AnalyticSetOperations
from .operations.asset_operations import AssetOperations
from .operations.database_operations import DatabaseOperations
from .operations.ems_profile_operations import EmsProfileOperations
from .operations.ems_securable_operations import EmsSecurableOperations
from .operations.ems_system_operations import EmsSystemOperations
from .operations.export_service_operations import ExportServiceOperations
from .operations.html_documentation_operations import HtmlDocumentationOperations
from .operations.identification_operations import IdentificationOperations
from .operations.navigation_operations import NavigationOperations
from .operations.parameter_set_operations import ParameterSetOperations
from .operations.profile_operations import ProfileOperations
from .operations.tableau_operations import TableauOperations
from .operations.trajectory_operations import TrajectoryOperations
from .operations.transfer_operations import TransferOperations
from .operations.upload_operations import UploadOperations
from .operations.weather_operations import WeatherOperations
from . import models


class emsapiConfiguration(Configuration):
    """Configuration for emsapi
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://d1mo-api.us.efoqa.com:443/api'

        super(emsapiConfiguration, self).__init__(base_url)

        self.add_user_agent('emsapi/{}'.format(VERSION))

        self.credentials = credentials


class emsapi(SDKClient):
    """The second version of the REST-based API for accessing EMS data

    :ivar config: Configuration for client.
    :vartype config: emsapiConfiguration

    :ivar admin_api_client: AdminApiClient operations
    :vartype admin_api_client: emsapi.operations.AdminApiClientOperations
    :ivar admin_application: AdminApplication operations
    :vartype admin_application: emsapi.operations.AdminApplicationOperations
    :ivar admin_dashboard: AdminDashboard operations
    :vartype admin_dashboard: emsapi.operations.AdminDashboardOperations
    :ivar admin_ems_securable: AdminEmsSecurable operations
    :vartype admin_ems_securable: emsapi.operations.AdminEmsSecurableOperations
    :ivar admin_ems_system: AdminEmsSystem operations
    :vartype admin_ems_system: emsapi.operations.AdminEmsSystemOperations
    :ivar admin_group: AdminGroup operations
    :vartype admin_group: emsapi.operations.AdminGroupOperations
    :ivar admin_user: AdminUser operations
    :vartype admin_user: emsapi.operations.AdminUserOperations
    :ivar alert: Alert operations
    :vartype alert: emsapi.operations.AlertOperations
    :ivar analytic: Analytic operations
    :vartype analytic: emsapi.operations.AnalyticOperations
    :ivar analytic_set: AnalyticSet operations
    :vartype analytic_set: emsapi.operations.AnalyticSetOperations
    :ivar asset: Asset operations
    :vartype asset: emsapi.operations.AssetOperations
    :ivar database: Database operations
    :vartype database: emsapi.operations.DatabaseOperations
    :ivar ems_profile: EmsProfile operations
    :vartype ems_profile: emsapi.operations.EmsProfileOperations
    :ivar ems_securable: EmsSecurable operations
    :vartype ems_securable: emsapi.operations.EmsSecurableOperations
    :ivar ems_system: EmsSystem operations
    :vartype ems_system: emsapi.operations.EmsSystemOperations
    :ivar export_service: ExportService operations
    :vartype export_service: emsapi.operations.ExportServiceOperations
    :ivar html_documentation: HtmlDocumentation operations
    :vartype html_documentation: emsapi.operations.HtmlDocumentationOperations
    :ivar identification: Identification operations
    :vartype identification: emsapi.operations.IdentificationOperations
    :ivar navigation: Navigation operations
    :vartype navigation: emsapi.operations.NavigationOperations
    :ivar parameter_set: ParameterSet operations
    :vartype parameter_set: emsapi.operations.ParameterSetOperations
    :ivar profile: Profile operations
    :vartype profile: emsapi.operations.ProfileOperations
    :ivar tableau: Tableau operations
    :vartype tableau: emsapi.operations.TableauOperations
    :ivar trajectory: Trajectory operations
    :vartype trajectory: emsapi.operations.TrajectoryOperations
    :ivar transfer: Transfer operations
    :vartype transfer: emsapi.operations.TransferOperations
    :ivar upload: Upload operations
    :vartype upload: emsapi.operations.UploadOperations
    :ivar weather: Weather operations
    :vartype weather: emsapi.operations.WeatherOperations

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = emsapiConfiguration(credentials, base_url)
        super(emsapi, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = 'v2'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.admin_api_client = AdminApiClientOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.admin_application = AdminApplicationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.admin_dashboard = AdminDashboardOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.admin_ems_securable = AdminEmsSecurableOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.admin_ems_system = AdminEmsSystemOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.admin_group = AdminGroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.admin_user = AdminUserOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alert = AlertOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.analytic = AnalyticOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.analytic_set = AnalyticSetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.asset = AssetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.database = DatabaseOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.ems_profile = EmsProfileOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.ems_securable = EmsSecurableOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.ems_system = EmsSystemOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.export_service = ExportServiceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.html_documentation = HtmlDocumentationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.identification = IdentificationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.navigation = NavigationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.parameter_set = ParameterSetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.profile = ProfileOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tableau = TableauOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.trajectory = TrajectoryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.transfer = TransferOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.upload = UploadOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.weather = WeatherOperations(
            self._client, self.config, self._serialize, self._deserialize)

    @staticmethod
    def create(username, password, url):
        """Creates a new instance of EMS API client. This client will automatically manage 
        API tokens for the given username/password.
        
        :param username: The username to use for authentication.
        :type username: str
        :param password: The password to use for authentication.
        :type password: str
        :param url: The EMS API endpoint to connect to. This should include the /api part at the end of the URL.
        :type url: str
        """
        from .extensions import EmsApiTokenAuthentication
        credentials = EmsApiTokenAuthentication(username, password, url)
        client = emsapi(credentials, url)
        credentials.set_config(client.config)
        return client

    def find_ems_system_id(self, name):
        """Finds the EMS system id for the given name.
        
        :param name: The EMS system name to search for.
        :type name: str
        """
        from .extensions import EmsSystemHelper
        return EmsSystemHelper.find_id(self, name)

    def is_error(self, response):
        """Returns True if the response represents an error"""
        from .extensions import ErrorHelper
        return ErrorHelper.is_error(response)

    def get_error_message(self, response):
        """Returns the error message if there was an error in the request, or None otherwise"""
        from .extensions import ErrorHelper
        return ErrorHelper.get_error_message(response)
