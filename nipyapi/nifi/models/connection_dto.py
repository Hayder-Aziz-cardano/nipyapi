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


class ConnectionDTO(object):
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
        'id': 'str',
        'versioned_component_id': 'str',
        'parent_group_id': 'str',
        'position': 'PositionDTO',
        'source': 'ConnectableDTO',
        'destination': 'ConnectableDTO',
        'name': 'str',
        'label_index': 'int',
        'getz_index': 'int',
        'selected_relationships': 'list[str]',
        'available_relationships': 'list[str]',
        'back_pressure_object_threshold': 'int',
        'back_pressure_data_size_threshold': 'str',
        'flow_file_expiration': 'str',
        'prioritizers': 'list[str]',
        'bends': 'list[PositionDTO]',
        'load_balance_strategy': 'str',
        'load_balance_partition_attribute': 'str',
        'load_balance_compression': 'str',
        'load_balance_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'versioned_component_id': 'versionedComponentId',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'source': 'source',
        'destination': 'destination',
        'name': 'name',
        'label_index': 'labelIndex',
        'getz_index': 'getzIndex',
        'selected_relationships': 'selectedRelationships',
        'available_relationships': 'availableRelationships',
        'back_pressure_object_threshold': 'backPressureObjectThreshold',
        'back_pressure_data_size_threshold': 'backPressureDataSizeThreshold',
        'flow_file_expiration': 'flowFileExpiration',
        'prioritizers': 'prioritizers',
        'bends': 'bends',
        'load_balance_strategy': 'loadBalanceStrategy',
        'load_balance_partition_attribute': 'loadBalancePartitionAttribute',
        'load_balance_compression': 'loadBalanceCompression',
        'load_balance_status': 'loadBalanceStatus'
    }

    def __init__(self, id=None, versioned_component_id=None, parent_group_id=None, position=None, source=None, destination=None, name=None, label_index=None, getz_index=None, selected_relationships=None, available_relationships=None, back_pressure_object_threshold=None, back_pressure_data_size_threshold=None, flow_file_expiration=None, prioritizers=None, bends=None, load_balance_strategy=None, load_balance_partition_attribute=None, load_balance_compression=None, load_balance_status=None):
        """
        ConnectionDTO - a model defined in Swagger
        """

        self._id = None
        self._versioned_component_id = None
        self._parent_group_id = None
        self._position = None
        self._source = None
        self._destination = None
        self._name = None
        self._label_index = None
        self._getz_index = None
        self._selected_relationships = None
        self._available_relationships = None
        self._back_pressure_object_threshold = None
        self._back_pressure_data_size_threshold = None
        self._flow_file_expiration = None
        self._prioritizers = None
        self._bends = None
        self._load_balance_strategy = None
        self._load_balance_partition_attribute = None
        self._load_balance_compression = None
        self._load_balance_status = None

        if id is not None:
          self.id = id
        if versioned_component_id is not None:
          self.versioned_component_id = versioned_component_id
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if position is not None:
          self.position = position
        if source is not None:
          self.source = source
        if destination is not None:
          self.destination = destination
        if name is not None:
          self.name = name
        if label_index is not None:
          self.label_index = label_index
        if getz_index is not None:
          self.getz_index = getz_index
        if selected_relationships is not None:
          self.selected_relationships = selected_relationships
        if available_relationships is not None:
          self.available_relationships = available_relationships
        if back_pressure_object_threshold is not None:
          self.back_pressure_object_threshold = back_pressure_object_threshold
        if back_pressure_data_size_threshold is not None:
          self.back_pressure_data_size_threshold = back_pressure_data_size_threshold
        if flow_file_expiration is not None:
          self.flow_file_expiration = flow_file_expiration
        if prioritizers is not None:
          self.prioritizers = prioritizers
        if bends is not None:
          self.bends = bends
        if load_balance_strategy is not None:
          self.load_balance_strategy = load_balance_strategy
        if load_balance_partition_attribute is not None:
          self.load_balance_partition_attribute = load_balance_partition_attribute
        if load_balance_compression is not None:
          self.load_balance_compression = load_balance_compression
        if load_balance_status is not None:
          self.load_balance_status = load_balance_status

    @property
    def id(self):
        """
        Gets the id of this ConnectionDTO.
        The id of the component.

        :return: The id of this ConnectionDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionDTO.
        The id of the component.

        :param id: The id of this ConnectionDTO.
        :type: str
        """

        self._id = id

    @property
    def versioned_component_id(self):
        """
        Gets the versioned_component_id of this ConnectionDTO.
        The ID of the corresponding component that is under version control

        :return: The versioned_component_id of this ConnectionDTO.
        :rtype: str
        """
        return self._versioned_component_id

    @versioned_component_id.setter
    def versioned_component_id(self, versioned_component_id):
        """
        Sets the versioned_component_id of this ConnectionDTO.
        The ID of the corresponding component that is under version control

        :param versioned_component_id: The versioned_component_id of this ConnectionDTO.
        :type: str
        """

        self._versioned_component_id = versioned_component_id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this ConnectionDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this ConnectionDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this ConnectionDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this ConnectionDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this ConnectionDTO.
        The position of this component in the UI if applicable.

        :return: The position of this ConnectionDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ConnectionDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this ConnectionDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def source(self):
        """
        Gets the source of this ConnectionDTO.
        The source of the connection.

        :return: The source of this ConnectionDTO.
        :rtype: ConnectableDTO
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ConnectionDTO.
        The source of the connection.

        :param source: The source of this ConnectionDTO.
        :type: ConnectableDTO
        """

        self._source = source

    @property
    def destination(self):
        """
        Gets the destination of this ConnectionDTO.
        The destination of the connection.

        :return: The destination of this ConnectionDTO.
        :rtype: ConnectableDTO
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this ConnectionDTO.
        The destination of the connection.

        :param destination: The destination of this ConnectionDTO.
        :type: ConnectableDTO
        """

        self._destination = destination

    @property
    def name(self):
        """
        Gets the name of this ConnectionDTO.
        The name of the connection.

        :return: The name of this ConnectionDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectionDTO.
        The name of the connection.

        :param name: The name of this ConnectionDTO.
        :type: str
        """

        self._name = name

    @property
    def label_index(self):
        """
        Gets the label_index of this ConnectionDTO.
        The index of the bend point where to place the connection label.

        :return: The label_index of this ConnectionDTO.
        :rtype: int
        """
        return self._label_index

    @label_index.setter
    def label_index(self, label_index):
        """
        Sets the label_index of this ConnectionDTO.
        The index of the bend point where to place the connection label.

        :param label_index: The label_index of this ConnectionDTO.
        :type: int
        """

        self._label_index = label_index

    @property
    def getz_index(self):
        """
        Gets the getz_index of this ConnectionDTO.
        The z index of the connection.

        :return: The getz_index of this ConnectionDTO.
        :rtype: int
        """
        return self._getz_index

    @getz_index.setter
    def getz_index(self, getz_index):
        """
        Sets the getz_index of this ConnectionDTO.
        The z index of the connection.

        :param getz_index: The getz_index of this ConnectionDTO.
        :type: int
        """

        self._getz_index = getz_index

    @property
    def selected_relationships(self):
        """
        Gets the selected_relationships of this ConnectionDTO.
        The selected relationship that comprise the connection.

        :return: The selected_relationships of this ConnectionDTO.
        :rtype: list[str]
        """
        return self._selected_relationships

    @selected_relationships.setter
    def selected_relationships(self, selected_relationships):
        """
        Sets the selected_relationships of this ConnectionDTO.
        The selected relationship that comprise the connection.

        :param selected_relationships: The selected_relationships of this ConnectionDTO.
        :type: list[str]
        """

        self._selected_relationships = selected_relationships

    @property
    def available_relationships(self):
        """
        Gets the available_relationships of this ConnectionDTO.
        The relationships that the source of the connection currently supports.

        :return: The available_relationships of this ConnectionDTO.
        :rtype: list[str]
        """
        return self._available_relationships

    @available_relationships.setter
    def available_relationships(self, available_relationships):
        """
        Sets the available_relationships of this ConnectionDTO.
        The relationships that the source of the connection currently supports.

        :param available_relationships: The available_relationships of this ConnectionDTO.
        :type: list[str]
        """

        self._available_relationships = available_relationships

    @property
    def back_pressure_object_threshold(self):
        """
        Gets the back_pressure_object_threshold of this ConnectionDTO.
        The object count threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :return: The back_pressure_object_threshold of this ConnectionDTO.
        :rtype: int
        """
        return self._back_pressure_object_threshold

    @back_pressure_object_threshold.setter
    def back_pressure_object_threshold(self, back_pressure_object_threshold):
        """
        Sets the back_pressure_object_threshold of this ConnectionDTO.
        The object count threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :param back_pressure_object_threshold: The back_pressure_object_threshold of this ConnectionDTO.
        :type: int
        """

        self._back_pressure_object_threshold = back_pressure_object_threshold

    @property
    def back_pressure_data_size_threshold(self):
        """
        Gets the back_pressure_data_size_threshold of this ConnectionDTO.
        The object data size threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :return: The back_pressure_data_size_threshold of this ConnectionDTO.
        :rtype: str
        """
        return self._back_pressure_data_size_threshold

    @back_pressure_data_size_threshold.setter
    def back_pressure_data_size_threshold(self, back_pressure_data_size_threshold):
        """
        Sets the back_pressure_data_size_threshold of this ConnectionDTO.
        The object data size threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :param back_pressure_data_size_threshold: The back_pressure_data_size_threshold of this ConnectionDTO.
        :type: str
        """

        self._back_pressure_data_size_threshold = back_pressure_data_size_threshold

    @property
    def flow_file_expiration(self):
        """
        Gets the flow_file_expiration of this ConnectionDTO.
        The amount of time a flow file may be in the flow before it will be automatically aged out of the flow. Once a flow file reaches this age it will be terminated from the flow the next time a processor attempts to start work on it.

        :return: The flow_file_expiration of this ConnectionDTO.
        :rtype: str
        """
        return self._flow_file_expiration

    @flow_file_expiration.setter
    def flow_file_expiration(self, flow_file_expiration):
        """
        Sets the flow_file_expiration of this ConnectionDTO.
        The amount of time a flow file may be in the flow before it will be automatically aged out of the flow. Once a flow file reaches this age it will be terminated from the flow the next time a processor attempts to start work on it.

        :param flow_file_expiration: The flow_file_expiration of this ConnectionDTO.
        :type: str
        """

        self._flow_file_expiration = flow_file_expiration

    @property
    def prioritizers(self):
        """
        Gets the prioritizers of this ConnectionDTO.
        The comparators used to prioritize the queue.

        :return: The prioritizers of this ConnectionDTO.
        :rtype: list[str]
        """
        return self._prioritizers

    @prioritizers.setter
    def prioritizers(self, prioritizers):
        """
        Sets the prioritizers of this ConnectionDTO.
        The comparators used to prioritize the queue.

        :param prioritizers: The prioritizers of this ConnectionDTO.
        :type: list[str]
        """

        self._prioritizers = prioritizers

    @property
    def bends(self):
        """
        Gets the bends of this ConnectionDTO.
        The bend points on the connection.

        :return: The bends of this ConnectionDTO.
        :rtype: list[PositionDTO]
        """
        return self._bends

    @bends.setter
    def bends(self, bends):
        """
        Sets the bends of this ConnectionDTO.
        The bend points on the connection.

        :param bends: The bends of this ConnectionDTO.
        :type: list[PositionDTO]
        """

        self._bends = bends

    @property
    def load_balance_strategy(self):
        """
        Gets the load_balance_strategy of this ConnectionDTO.
        How to load balance the data in this Connection across the nodes in the cluster.

        :return: The load_balance_strategy of this ConnectionDTO.
        :rtype: str
        """
        return self._load_balance_strategy

    @load_balance_strategy.setter
    def load_balance_strategy(self, load_balance_strategy):
        """
        Sets the load_balance_strategy of this ConnectionDTO.
        How to load balance the data in this Connection across the nodes in the cluster.

        :param load_balance_strategy: The load_balance_strategy of this ConnectionDTO.
        :type: str
        """
        allowed_values = ["DO_NOT_LOAD_BALANCE", "PARTITION_BY_ATTRIBUTE", "ROUND_ROBIN", "SINGLE_NODE"]
        if load_balance_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `load_balance_strategy` ({0}), must be one of {1}"
                .format(load_balance_strategy, allowed_values)
            )

        self._load_balance_strategy = load_balance_strategy

    @property
    def load_balance_partition_attribute(self):
        """
        Gets the load_balance_partition_attribute of this ConnectionDTO.
        The FlowFile Attribute to use for determining which node a FlowFile will go to if the Load Balancing Strategy is set to PARTITION_BY_ATTRIBUTE

        :return: The load_balance_partition_attribute of this ConnectionDTO.
        :rtype: str
        """
        return self._load_balance_partition_attribute

    @load_balance_partition_attribute.setter
    def load_balance_partition_attribute(self, load_balance_partition_attribute):
        """
        Sets the load_balance_partition_attribute of this ConnectionDTO.
        The FlowFile Attribute to use for determining which node a FlowFile will go to if the Load Balancing Strategy is set to PARTITION_BY_ATTRIBUTE

        :param load_balance_partition_attribute: The load_balance_partition_attribute of this ConnectionDTO.
        :type: str
        """

        self._load_balance_partition_attribute = load_balance_partition_attribute

    @property
    def load_balance_compression(self):
        """
        Gets the load_balance_compression of this ConnectionDTO.
        Whether or not data should be compressed when being transferred between nodes in the cluster.

        :return: The load_balance_compression of this ConnectionDTO.
        :rtype: str
        """
        return self._load_balance_compression

    @load_balance_compression.setter
    def load_balance_compression(self, load_balance_compression):
        """
        Sets the load_balance_compression of this ConnectionDTO.
        Whether or not data should be compressed when being transferred between nodes in the cluster.

        :param load_balance_compression: The load_balance_compression of this ConnectionDTO.
        :type: str
        """
        allowed_values = ["DO_NOT_COMPRESS", "COMPRESS_ATTRIBUTES_ONLY", "COMPRESS_ATTRIBUTES_AND_CONTENT"]
        if load_balance_compression not in allowed_values:
            raise ValueError(
                "Invalid value for `load_balance_compression` ({0}), must be one of {1}"
                .format(load_balance_compression, allowed_values)
            )

        self._load_balance_compression = load_balance_compression

    @property
    def load_balance_status(self):
        """
        Gets the load_balance_status of this ConnectionDTO.
        The current status of the Connection's Load Balancing Activities. Status can indicate that Load Balancing is not configured for the connection, that Load Balancing is configured but inactive (not currently transferring data to another node), or that Load Balancing is configured and actively transferring data to another node.

        :return: The load_balance_status of this ConnectionDTO.
        :rtype: str
        """
        return self._load_balance_status

    @load_balance_status.setter
    def load_balance_status(self, load_balance_status):
        """
        Sets the load_balance_status of this ConnectionDTO.
        The current status of the Connection's Load Balancing Activities. Status can indicate that Load Balancing is not configured for the connection, that Load Balancing is configured but inactive (not currently transferring data to another node), or that Load Balancing is configured and actively transferring data to another node.

        :param load_balance_status: The load_balance_status of this ConnectionDTO.
        :type: str
        """
        allowed_values = ["LOAD_BALANCE_NOT_CONFIGURED", "LOAD_BALANCE_INACTIVE", "LOAD_BALANCE_ACTIVE"]
        if load_balance_status not in allowed_values:
            raise ValueError(
                "Invalid value for `load_balance_status` ({0}), must be one of {1}"
                .format(load_balance_status, allowed_values)
            )

        self._load_balance_status = load_balance_status

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
        if not isinstance(other, ConnectionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
