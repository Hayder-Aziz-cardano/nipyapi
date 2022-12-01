# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.19.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FlowsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_available_flow_fields(self, **kwargs):
        """
        Get flow fields
        Retrieves the flow field names that can be used for searching or sorting on flows.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_flow_fields(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Fields
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_available_flow_fields_with_http_info(**kwargs)
        else:
            (data) = self.get_available_flow_fields_with_http_info(**kwargs)
            return data

    def get_available_flow_fields_with_http_info(self, **kwargs):
        """
        Get flow fields
        Retrieves the flow field names that can be used for searching or sorting on flows.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_flow_fields_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Fields
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_flow_fields" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/flows/fields', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Fields',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def global_get_flow(self, flow_id, **kwargs):
        """
        Get flow
        Gets a flow by id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_flow(flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :return: VersionedFlow
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.global_get_flow_with_http_info(flow_id, **kwargs)
        else:
            (data) = self.global_get_flow_with_http_info(flow_id, **kwargs)
            return data

    def global_get_flow_with_http_info(self, flow_id, **kwargs):
        """
        Get flow
        Gets a flow by id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_flow_with_http_info(flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :return: VersionedFlow
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flow_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method global_get_flow" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flow_id' is set
        if ('flow_id' not in params) or (params['flow_id'] is None):
            raise ValueError("Missing the required parameter `flow_id` when calling `global_get_flow`")


        collection_formats = {}

        path_params = {}
        if 'flow_id' in params:
            path_params['flowId'] = params['flow_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/flows/{flowId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VersionedFlow',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def global_get_flow_version(self, flow_id, version_number, **kwargs):
        """
        Get flow version
        Gets the given version of a flow, including metadata and flow content.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_flow_version(flow_id, version_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :param int version_number: The version number (required)
        :return: VersionedFlowSnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.global_get_flow_version_with_http_info(flow_id, version_number, **kwargs)
        else:
            (data) = self.global_get_flow_version_with_http_info(flow_id, version_number, **kwargs)
            return data

    def global_get_flow_version_with_http_info(self, flow_id, version_number, **kwargs):
        """
        Get flow version
        Gets the given version of a flow, including metadata and flow content.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_flow_version_with_http_info(flow_id, version_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :param int version_number: The version number (required)
        :return: VersionedFlowSnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flow_id', 'version_number']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method global_get_flow_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flow_id' is set
        if ('flow_id' not in params) or (params['flow_id'] is None):
            raise ValueError("Missing the required parameter `flow_id` when calling `global_get_flow_version`")
        # verify the required parameter 'version_number' is set
        if ('version_number' not in params) or (params['version_number'] is None):
            raise ValueError("Missing the required parameter `version_number` when calling `global_get_flow_version`")

        if 'version_number' in params and not re.search('\\d+', params['version_number']):
            raise ValueError("Invalid value for parameter `version_number` when calling `global_get_flow_version`, must conform to the pattern `/\\d+/`")

        collection_formats = {}

        path_params = {}
        if 'flow_id' in params:
            path_params['flowId'] = params['flow_id']
        if 'version_number' in params:
            path_params['versionNumber'] = params['version_number']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/flows/{flowId}/versions/{versionNumber}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VersionedFlowSnapshot',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def global_get_flow_versions(self, flow_id, **kwargs):
        """
        Get flow versions
        Gets summary information for all versions of a given flow. Versions are ordered newest->oldest.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_flow_versions(flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :return: list[VersionedFlowSnapshotMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.global_get_flow_versions_with_http_info(flow_id, **kwargs)
        else:
            (data) = self.global_get_flow_versions_with_http_info(flow_id, **kwargs)
            return data

    def global_get_flow_versions_with_http_info(self, flow_id, **kwargs):
        """
        Get flow versions
        Gets summary information for all versions of a given flow. Versions are ordered newest->oldest.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_flow_versions_with_http_info(flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :return: list[VersionedFlowSnapshotMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flow_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method global_get_flow_versions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flow_id' is set
        if ('flow_id' not in params) or (params['flow_id'] is None):
            raise ValueError("Missing the required parameter `flow_id` when calling `global_get_flow_versions`")


        collection_formats = {}

        path_params = {}
        if 'flow_id' in params:
            path_params['flowId'] = params['flow_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/flows/{flowId}/versions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[VersionedFlowSnapshotMetadata]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def global_get_latest_flow_version(self, flow_id, **kwargs):
        """
        Get latest flow version
        Gets the latest version of a flow, including metadata and flow content.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_latest_flow_version(flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :return: VersionedFlowSnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.global_get_latest_flow_version_with_http_info(flow_id, **kwargs)
        else:
            (data) = self.global_get_latest_flow_version_with_http_info(flow_id, **kwargs)
            return data

    def global_get_latest_flow_version_with_http_info(self, flow_id, **kwargs):
        """
        Get latest flow version
        Gets the latest version of a flow, including metadata and flow content.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_latest_flow_version_with_http_info(flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :return: VersionedFlowSnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flow_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method global_get_latest_flow_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flow_id' is set
        if ('flow_id' not in params) or (params['flow_id'] is None):
            raise ValueError("Missing the required parameter `flow_id` when calling `global_get_latest_flow_version`")


        collection_formats = {}

        path_params = {}
        if 'flow_id' in params:
            path_params['flowId'] = params['flow_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/flows/{flowId}/versions/latest', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VersionedFlowSnapshot',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def global_get_latest_flow_version_metadata(self, flow_id, **kwargs):
        """
        Get latest flow version metadata
        Gets the metadata for the latest version of a flow.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_latest_flow_version_metadata(flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :return: VersionedFlowSnapshotMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.global_get_latest_flow_version_metadata_with_http_info(flow_id, **kwargs)
        else:
            (data) = self.global_get_latest_flow_version_metadata_with_http_info(flow_id, **kwargs)
            return data

    def global_get_latest_flow_version_metadata_with_http_info(self, flow_id, **kwargs):
        """
        Get latest flow version metadata
        Gets the metadata for the latest version of a flow.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.global_get_latest_flow_version_metadata_with_http_info(flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str flow_id: The flow identifier (required)
        :return: VersionedFlowSnapshotMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flow_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method global_get_latest_flow_version_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flow_id' is set
        if ('flow_id' not in params) or (params['flow_id'] is None):
            raise ValueError("Missing the required parameter `flow_id` when calling `global_get_latest_flow_version_metadata`")


        collection_formats = {}

        path_params = {}
        if 'flow_id' in params:
            path_params['flowId'] = params['flow_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/flows/{flowId}/versions/latest/metadata', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VersionedFlowSnapshotMetadata',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
