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

from .resource import Resource


class GeoRegion(Resource):
    """Geographical region.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :param name: Resource Name.
    :type name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :param type: Resource type.
    :type type: str
    :param tags: Resource tags.
    :type tags: dict
    :ivar geo_region_name: Region name.
    :vartype geo_region_name: str
    :ivar description: Region description.
    :vartype description: str
    :ivar display_name: Display name for region.
    :vartype display_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'location': {'required': True},
        'geo_region_name': {'readonly': True},
        'description': {'readonly': True},
        'display_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'geo_region_name': {'key': 'properties.name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
    }

    def __init__(self, name, location, kind=None, type=None, tags=None):
        super(GeoRegion, self).__init__(name=name, kind=kind, location=location, type=type, tags=tags)
        self.geo_region_name = None
        self.description = None
        self.display_name = None
