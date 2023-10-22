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


class ParameterContextValidationRequestEntity(object):
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
        'request': 'ParameterContextValidationRequestDTO',
        'disconnected_node_acknowledged': 'bool'
    }

    attribute_map = {
        'request': 'request',
        'disconnected_node_acknowledged': 'disconnectedNodeAcknowledged'
    }

    def __init__(self, request=None, disconnected_node_acknowledged=None):
        """
        ParameterContextValidationRequestEntity - a model defined in Swagger
        """

        self._request = None
        self._disconnected_node_acknowledged = None

        if request is not None:
          self.request = request
        if disconnected_node_acknowledged is not None:
          self.disconnected_node_acknowledged = disconnected_node_acknowledged

    @property
    def request(self):
        """
        Gets the request of this ParameterContextValidationRequestEntity.
        The Update Request

        :return: The request of this ParameterContextValidationRequestEntity.
        :rtype: ParameterContextValidationRequestDTO
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this ParameterContextValidationRequestEntity.
        The Update Request

        :param request: The request of this ParameterContextValidationRequestEntity.
        :type: ParameterContextValidationRequestDTO
        """

        self._request = request

    @property
    def disconnected_node_acknowledged(self):
        """
        Gets the disconnected_node_acknowledged of this ParameterContextValidationRequestEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :return: The disconnected_node_acknowledged of this ParameterContextValidationRequestEntity.
        :rtype: bool
        """
        return self._disconnected_node_acknowledged

    @disconnected_node_acknowledged.setter
    def disconnected_node_acknowledged(self, disconnected_node_acknowledged):
        """
        Sets the disconnected_node_acknowledged of this ParameterContextValidationRequestEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :param disconnected_node_acknowledged: The disconnected_node_acknowledged of this ParameterContextValidationRequestEntity.
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
        if not isinstance(other, ParameterContextValidationRequestEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
