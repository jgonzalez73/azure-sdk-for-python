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


class SourceControl(Resource):
    """The source control OAuth token.

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
    :param source_control_name: Name or source control type.
    :type source_control_name: str
    :param token: OAuth access token.
    :type token: str
    :param token_secret: OAuth access token secret.
    :type token_secret: str
    :param refresh_token: OAuth refresh token.
    :type refresh_token: str
    :param expiration_time: OAuth token expiration.
    :type expiration_time: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'source_control_name': {'key': 'properties.name', 'type': 'str'},
        'token': {'key': 'properties.token', 'type': 'str'},
        'token_secret': {'key': 'properties.tokenSecret', 'type': 'str'},
        'refresh_token': {'key': 'properties.refreshToken', 'type': 'str'},
        'expiration_time': {'key': 'properties.expirationTime', 'type': 'iso-8601'},
    }

    def __init__(self, name, location, kind=None, type=None, tags=None, source_control_name=None, token=None, token_secret=None, refresh_token=None, expiration_time=None):
        super(SourceControl, self).__init__(name=name, kind=kind, location=location, type=type, tags=tags)
        self.source_control_name = source_control_name
        self.token = token
        self.token_secret = token_secret
        self.refresh_token = refresh_token
        self.expiration_time = expiration_time
