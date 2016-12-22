# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloningInfo(Model):
    """Information needed for cloning operation.

    :param correlation_id: Correlation ID of cloning operation. This ID ties
     multiple cloning operations
     together to use the same snapshot.
    :type correlation_id: str
    :param overwrite: <code>true</code> to overwrite destination app;
     otherwise, <code>false</code>.
    :type overwrite: bool
    :param clone_custom_host_names: <code>true</code> to clone custom
     hostnames from source app; otherwise, <code>false</code>.
    :type clone_custom_host_names: bool
    :param clone_source_control: <code>true</code> to clone source control
     from source app; otherwise, <code>false</code>.
    :type clone_source_control: bool
    :param source_web_app_id: ARM resource ID of the source app. App resource
     ID is of the form
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}
     for production slots and
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName}
     for other slots.
    :type source_web_app_id: str
    :param hosting_environment: App Service Environment.
    :type hosting_environment: str
    :param app_settings_overrides: Application setting overrides for cloned
     app. If specified, these settings override the settings cloned
     from source app. Otherwise, application settings from source app are
     retained.
    :type app_settings_overrides: dict
    :param configure_load_balancing: <code>true</code> to configure load
     balancing for source and destination app.
    :type configure_load_balancing: bool
    :param traffic_manager_profile_id: ARM resource ID of the Traffic Manager
     profile to use, if it exists. Traffic Manager resource ID is of the form
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{profileName}.
    :type traffic_manager_profile_id: str
    :param traffic_manager_profile_name: Name of Traffic Manager profile to
     create. This is only needed if Traffic Manager profile does not already
     exist.
    :type traffic_manager_profile_name: str
    """

    _validation = {
        'source_web_app_id': {'required': True},
    }

    _attribute_map = {
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'overwrite': {'key': 'overwrite', 'type': 'bool'},
        'clone_custom_host_names': {'key': 'cloneCustomHostNames', 'type': 'bool'},
        'clone_source_control': {'key': 'cloneSourceControl', 'type': 'bool'},
        'source_web_app_id': {'key': 'sourceWebAppId', 'type': 'str'},
        'hosting_environment': {'key': 'hostingEnvironment', 'type': 'str'},
        'app_settings_overrides': {'key': 'appSettingsOverrides', 'type': '{str}'},
        'configure_load_balancing': {'key': 'configureLoadBalancing', 'type': 'bool'},
        'traffic_manager_profile_id': {'key': 'trafficManagerProfileId', 'type': 'str'},
        'traffic_manager_profile_name': {'key': 'trafficManagerProfileName', 'type': 'str'},
    }

    def __init__(self, source_web_app_id, correlation_id=None, overwrite=None, clone_custom_host_names=None, clone_source_control=None, hosting_environment=None, app_settings_overrides=None, configure_load_balancing=None, traffic_manager_profile_id=None, traffic_manager_profile_name=None):
        self.correlation_id = correlation_id
        self.overwrite = overwrite
        self.clone_custom_host_names = clone_custom_host_names
        self.clone_source_control = clone_source_control
        self.source_web_app_id = source_web_app_id
        self.hosting_environment = hosting_environment
        self.app_settings_overrides = app_settings_overrides
        self.configure_load_balancing = configure_load_balancing
        self.traffic_manager_profile_id = traffic_manager_profile_id
        self.traffic_manager_profile_name = traffic_manager_profile_name
