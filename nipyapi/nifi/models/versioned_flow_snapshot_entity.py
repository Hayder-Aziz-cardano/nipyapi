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


class VersionedFlowSnapshotEntity(object):
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
        'versioned_flow_snapshot': 'RegisteredFlowSnapshot',
        'process_group_revision': 'RevisionDTO',
        'registry_id': 'str',
        'update_descendant_versioned_flows': 'bool',
        'disconnected_node_acknowledged': 'bool'
    }

    attribute_map = {
        'versioned_flow_snapshot': 'versionedFlowSnapshot',
        'process_group_revision': 'processGroupRevision',
        'registry_id': 'registryId',
        'update_descendant_versioned_flows': 'updateDescendantVersionedFlows',
        'disconnected_node_acknowledged': 'disconnectedNodeAcknowledged'
    }

    def __init__(self, versioned_flow_snapshot=None, process_group_revision=None, registry_id=None, update_descendant_versioned_flows=None, disconnected_node_acknowledged=None):
        """
        VersionedFlowSnapshotEntity - a model defined in Swagger
        """

        self._versioned_flow_snapshot = None
        self._process_group_revision = None
        self._registry_id = None
        self._update_descendant_versioned_flows = None
        self._disconnected_node_acknowledged = None

        if versioned_flow_snapshot is not None:
          self.versioned_flow_snapshot = versioned_flow_snapshot
        if process_group_revision is not None:
          self.process_group_revision = process_group_revision
        if registry_id is not None:
          self.registry_id = registry_id
        if update_descendant_versioned_flows is not None:
          self.update_descendant_versioned_flows = update_descendant_versioned_flows
        if disconnected_node_acknowledged is not None:
          self.disconnected_node_acknowledged = disconnected_node_acknowledged

    @property
    def versioned_flow_snapshot(self):
        """
        Gets the versioned_flow_snapshot of this VersionedFlowSnapshotEntity.
        The versioned flow snapshot

        :return: The versioned_flow_snapshot of this VersionedFlowSnapshotEntity.
        :rtype: RegisteredFlowSnapshot
        """
        return self._versioned_flow_snapshot

    @versioned_flow_snapshot.setter
    def versioned_flow_snapshot(self, versioned_flow_snapshot):
        """
        Sets the versioned_flow_snapshot of this VersionedFlowSnapshotEntity.
        The versioned flow snapshot

        :param versioned_flow_snapshot: The versioned_flow_snapshot of this VersionedFlowSnapshotEntity.
        :type: RegisteredFlowSnapshot
        """

        self._versioned_flow_snapshot = versioned_flow_snapshot

    @property
    def process_group_revision(self):
        """
        Gets the process_group_revision of this VersionedFlowSnapshotEntity.
        The Revision of the Process Group under Version Control

        :return: The process_group_revision of this VersionedFlowSnapshotEntity.
        :rtype: RevisionDTO
        """
        return self._process_group_revision

    @process_group_revision.setter
    def process_group_revision(self, process_group_revision):
        """
        Sets the process_group_revision of this VersionedFlowSnapshotEntity.
        The Revision of the Process Group under Version Control

        :param process_group_revision: The process_group_revision of this VersionedFlowSnapshotEntity.
        :type: RevisionDTO
        """

        self._process_group_revision = process_group_revision

    @property
    def registry_id(self):
        """
        Gets the registry_id of this VersionedFlowSnapshotEntity.
        The ID of the Registry that this flow belongs to

        :return: The registry_id of this VersionedFlowSnapshotEntity.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        """
        Sets the registry_id of this VersionedFlowSnapshotEntity.
        The ID of the Registry that this flow belongs to

        :param registry_id: The registry_id of this VersionedFlowSnapshotEntity.
        :type: str
        """

        self._registry_id = registry_id

    @property
    def update_descendant_versioned_flows(self):
        """
        Gets the update_descendant_versioned_flows of this VersionedFlowSnapshotEntity.
        If the Process Group to be updated has a child or descendant Process Group that is also under Version Control, this specifies whether or not the contents of that child/descendant Process Group should be updated.

        :return: The update_descendant_versioned_flows of this VersionedFlowSnapshotEntity.
        :rtype: bool
        """
        return self._update_descendant_versioned_flows

    @update_descendant_versioned_flows.setter
    def update_descendant_versioned_flows(self, update_descendant_versioned_flows):
        """
        Sets the update_descendant_versioned_flows of this VersionedFlowSnapshotEntity.
        If the Process Group to be updated has a child or descendant Process Group that is also under Version Control, this specifies whether or not the contents of that child/descendant Process Group should be updated.

        :param update_descendant_versioned_flows: The update_descendant_versioned_flows of this VersionedFlowSnapshotEntity.
        :type: bool
        """

        self._update_descendant_versioned_flows = update_descendant_versioned_flows

    @property
    def disconnected_node_acknowledged(self):
        """
        Gets the disconnected_node_acknowledged of this VersionedFlowSnapshotEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :return: The disconnected_node_acknowledged of this VersionedFlowSnapshotEntity.
        :rtype: bool
        """
        return self._disconnected_node_acknowledged

    @disconnected_node_acknowledged.setter
    def disconnected_node_acknowledged(self, disconnected_node_acknowledged):
        """
        Sets the disconnected_node_acknowledged of this VersionedFlowSnapshotEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :param disconnected_node_acknowledged: The disconnected_node_acknowledged of this VersionedFlowSnapshotEntity.
        :type: bool
        """

        self._disconnected_node_acknowledged = disconnected_node_acknowledged

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
        if not isinstance(other, VersionedFlowSnapshotEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
