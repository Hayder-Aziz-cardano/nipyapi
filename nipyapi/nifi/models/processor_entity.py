# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.23.2
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProcessorEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'revision': 'RevisionDTO',
        'id': 'str',
        'uri': 'str',
        'position': 'PositionDTO',
        'permissions': 'PermissionsDTO',
        'bulletins': 'list[BulletinEntity]',
        'disconnected_node_acknowledged': 'bool',
        'component': 'ProcessorDTO',
        'input_requirement': 'str',
        'status': 'ProcessorStatusDTO',
        'operate_permissions': 'PermissionsDTO'
    }

    attribute_map = {
        'revision': 'revision',
        'id': 'id',
        'uri': 'uri',
        'position': 'position',
        'permissions': 'permissions',
        'bulletins': 'bulletins',
        'disconnected_node_acknowledged': 'disconnectedNodeAcknowledged',
        'component': 'component',
        'input_requirement': 'inputRequirement',
        'status': 'status',
        'operate_permissions': 'operatePermissions'
    }

    def __init__(self, revision=None, id=None, uri=None, position=None, permissions=None, bulletins=None, disconnected_node_acknowledged=None, component=None, input_requirement=None, status=None, operate_permissions=None):
        """
        ProcessorEntity - a model defined in Swagger
        """

        self._revision = None
        self._id = None
        self._uri = None
        self._position = None
        self._permissions = None
        self._bulletins = None
        self._disconnected_node_acknowledged = None
        self._component = None
        self._input_requirement = None
        self._status = None
        self._operate_permissions = None

        if revision is not None:
          self.revision = revision
        if id is not None:
          self.id = id
        if uri is not None:
          self.uri = uri
        if position is not None:
          self.position = position
        if permissions is not None:
          self.permissions = permissions
        if bulletins is not None:
          self.bulletins = bulletins
        if disconnected_node_acknowledged is not None:
          self.disconnected_node_acknowledged = disconnected_node_acknowledged
        if component is not None:
          self.component = component
        if input_requirement is not None:
          self.input_requirement = input_requirement
        if status is not None:
          self.status = status
        if operate_permissions is not None:
          self.operate_permissions = operate_permissions

    @property
    def revision(self):
        """
        Gets the revision of this ProcessorEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :return: The revision of this ProcessorEntity.
        :rtype: RevisionDTO
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ProcessorEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :param revision: The revision of this ProcessorEntity.
        :type: RevisionDTO
        """

        self._revision = revision

    @property
    def id(self):
        """
        Gets the id of this ProcessorEntity.
        The id of the component.

        :return: The id of this ProcessorEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessorEntity.
        The id of the component.

        :param id: The id of this ProcessorEntity.
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """
        Gets the uri of this ProcessorEntity.
        The URI for futures requests to the component.

        :return: The uri of this ProcessorEntity.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ProcessorEntity.
        The URI for futures requests to the component.

        :param uri: The uri of this ProcessorEntity.
        :type: str
        """

        self._uri = uri

    @property
    def position(self):
        """
        Gets the position of this ProcessorEntity.
        The position of this component in the UI if applicable.

        :return: The position of this ProcessorEntity.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ProcessorEntity.
        The position of this component in the UI if applicable.

        :param position: The position of this ProcessorEntity.
        :type: PositionDTO
        """

        self._position = position

    @property
    def permissions(self):
        """
        Gets the permissions of this ProcessorEntity.
        The permissions for this component.

        :return: The permissions of this ProcessorEntity.
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this ProcessorEntity.
        The permissions for this component.

        :param permissions: The permissions of this ProcessorEntity.
        :type: PermissionsDTO
        """

        self._permissions = permissions

    @property
    def bulletins(self):
        """
        Gets the bulletins of this ProcessorEntity.
        The bulletins for this component.

        :return: The bulletins of this ProcessorEntity.
        :rtype: list[BulletinEntity]
        """
        return self._bulletins

    @bulletins.setter
    def bulletins(self, bulletins):
        """
        Sets the bulletins of this ProcessorEntity.
        The bulletins for this component.

        :param bulletins: The bulletins of this ProcessorEntity.
        :type: list[BulletinEntity]
        """

        self._bulletins = bulletins

    @property
    def disconnected_node_acknowledged(self):
        """
        Gets the disconnected_node_acknowledged of this ProcessorEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :return: The disconnected_node_acknowledged of this ProcessorEntity.
        :rtype: bool
        """
        return self._disconnected_node_acknowledged

    @disconnected_node_acknowledged.setter
    def disconnected_node_acknowledged(self, disconnected_node_acknowledged):
        """
        Sets the disconnected_node_acknowledged of this ProcessorEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :param disconnected_node_acknowledged: The disconnected_node_acknowledged of this ProcessorEntity.
        :type: bool
        """

        self._disconnected_node_acknowledged = disconnected_node_acknowledged

    @property
    def component(self):
        """
        Gets the component of this ProcessorEntity.

        :return: The component of this ProcessorEntity.
        :rtype: ProcessorDTO
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this ProcessorEntity.

        :param component: The component of this ProcessorEntity.
        :type: ProcessorDTO
        """

        self._component = component

    @property
    def input_requirement(self):
        """
        Gets the input_requirement of this ProcessorEntity.
        The input requirement for this processor.

        :return: The input_requirement of this ProcessorEntity.
        :rtype: str
        """
        return self._input_requirement

    @input_requirement.setter
    def input_requirement(self, input_requirement):
        """
        Sets the input_requirement of this ProcessorEntity.
        The input requirement for this processor.

        :param input_requirement: The input_requirement of this ProcessorEntity.
        :type: str
        """

        self._input_requirement = input_requirement

    @property
    def status(self):
        """
        Gets the status of this ProcessorEntity.

        :return: The status of this ProcessorEntity.
        :rtype: ProcessorStatusDTO
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProcessorEntity.

        :param status: The status of this ProcessorEntity.
        :type: ProcessorStatusDTO
        """

        self._status = status

    @property
    def operate_permissions(self):
        """
        Gets the operate_permissions of this ProcessorEntity.
        The permissions for this component operations.

        :return: The operate_permissions of this ProcessorEntity.
        :rtype: PermissionsDTO
        """
        return self._operate_permissions

    @operate_permissions.setter
    def operate_permissions(self, operate_permissions):
        """
        Sets the operate_permissions of this ProcessorEntity.
        The permissions for this component operations.

        :param operate_permissions: The operate_permissions of this ProcessorEntity.
        :type: PermissionsDTO
        """

        self._operate_permissions = operate_permissions

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProcessorEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
