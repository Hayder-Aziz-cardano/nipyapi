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


class AffectedComponentEntity(object):
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
        'component': 'AffectedComponentDTO',
        'process_group': 'ProcessGroupNameDTO',
        'reference_type': 'str'
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
        'process_group': 'processGroup',
        'reference_type': 'referenceType'
    }

    def __init__(self, revision=None, id=None, uri=None, position=None, permissions=None, bulletins=None, disconnected_node_acknowledged=None, component=None, process_group=None, reference_type=None):
        """
        AffectedComponentEntity - a model defined in Swagger
        """

        self._revision = None
        self._id = None
        self._uri = None
        self._position = None
        self._permissions = None
        self._bulletins = None
        self._disconnected_node_acknowledged = None
        self._component = None
        self._process_group = None
        self._reference_type = None

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
        if process_group is not None:
          self.process_group = process_group
        if reference_type is not None:
          self.reference_type = reference_type

    @property
    def revision(self):
        """
        Gets the revision of this AffectedComponentEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :return: The revision of this AffectedComponentEntity.
        :rtype: RevisionDTO
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this AffectedComponentEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :param revision: The revision of this AffectedComponentEntity.
        :type: RevisionDTO
        """

        self._revision = revision

    @property
    def id(self):
        """
        Gets the id of this AffectedComponentEntity.
        The id of the component.

        :return: The id of this AffectedComponentEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AffectedComponentEntity.
        The id of the component.

        :param id: The id of this AffectedComponentEntity.
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """
        Gets the uri of this AffectedComponentEntity.
        The URI for futures requests to the component.

        :return: The uri of this AffectedComponentEntity.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this AffectedComponentEntity.
        The URI for futures requests to the component.

        :param uri: The uri of this AffectedComponentEntity.
        :type: str
        """

        self._uri = uri

    @property
    def position(self):
        """
        Gets the position of this AffectedComponentEntity.
        The position of this component in the UI if applicable.

        :return: The position of this AffectedComponentEntity.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this AffectedComponentEntity.
        The position of this component in the UI if applicable.

        :param position: The position of this AffectedComponentEntity.
        :type: PositionDTO
        """

        self._position = position

    @property
    def permissions(self):
        """
        Gets the permissions of this AffectedComponentEntity.
        The permissions for this component.

        :return: The permissions of this AffectedComponentEntity.
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this AffectedComponentEntity.
        The permissions for this component.

        :param permissions: The permissions of this AffectedComponentEntity.
        :type: PermissionsDTO
        """

        self._permissions = permissions

    @property
    def bulletins(self):
        """
        Gets the bulletins of this AffectedComponentEntity.
        The bulletins for this component.

        :return: The bulletins of this AffectedComponentEntity.
        :rtype: list[BulletinEntity]
        """
        return self._bulletins

    @bulletins.setter
    def bulletins(self, bulletins):
        """
        Sets the bulletins of this AffectedComponentEntity.
        The bulletins for this component.

        :param bulletins: The bulletins of this AffectedComponentEntity.
        :type: list[BulletinEntity]
        """

        self._bulletins = bulletins

    @property
    def disconnected_node_acknowledged(self):
        """
        Gets the disconnected_node_acknowledged of this AffectedComponentEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :return: The disconnected_node_acknowledged of this AffectedComponentEntity.
        :rtype: bool
        """
        return self._disconnected_node_acknowledged

    @disconnected_node_acknowledged.setter
    def disconnected_node_acknowledged(self, disconnected_node_acknowledged):
        """
        Sets the disconnected_node_acknowledged of this AffectedComponentEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :param disconnected_node_acknowledged: The disconnected_node_acknowledged of this AffectedComponentEntity.
        :type: bool
        """

        self._disconnected_node_acknowledged = disconnected_node_acknowledged

    @property
    def component(self):
        """
        Gets the component of this AffectedComponentEntity.

        :return: The component of this AffectedComponentEntity.
        :rtype: AffectedComponentDTO
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this AffectedComponentEntity.

        :param component: The component of this AffectedComponentEntity.
        :type: AffectedComponentDTO
        """

        self._component = component

    @property
    def process_group(self):
        """
        Gets the process_group of this AffectedComponentEntity.
        The Process Group that the component belongs to

        :return: The process_group of this AffectedComponentEntity.
        :rtype: ProcessGroupNameDTO
        """
        return self._process_group

    @process_group.setter
    def process_group(self, process_group):
        """
        Sets the process_group of this AffectedComponentEntity.
        The Process Group that the component belongs to

        :param process_group: The process_group of this AffectedComponentEntity.
        :type: ProcessGroupNameDTO
        """

        self._process_group = process_group

    @property
    def reference_type(self):
        """
        Gets the reference_type of this AffectedComponentEntity.
        The type of component referenced

        :return: The reference_type of this AffectedComponentEntity.
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """
        Sets the reference_type of this AffectedComponentEntity.
        The type of component referenced

        :param reference_type: The reference_type of this AffectedComponentEntity.
        :type: str
        """
        allowed_values = ["PROCESSOR", "CONTROLLER_SERVICE", "INPUT_PORT", "OUTPUT_PORT", "REMOTE_INPUT_PORT", "REMOTE_OUTPUT_PORT"]
        if reference_type not in allowed_values:
            raise ValueError(
                "Invalid value for `reference_type` ({0}), must be one of {1}"
                .format(reference_type, allowed_values)
            )

        self._reference_type = reference_type

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
        if not isinstance(other, AffectedComponentEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
