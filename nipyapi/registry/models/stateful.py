# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.19.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Stateful(object):
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
        'description': 'str',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'scopes': 'scopes'
    }

    def __init__(self, description=None, scopes=None):
        """
        Stateful - a model defined in Swagger
        """

        self._description = None
        self._scopes = None

        if description is not None:
          self.description = description
        if scopes is not None:
          self.scopes = scopes

    @property
    def description(self):
        """
        Gets the description of this Stateful.
        The description for how the extension stores state

        :return: The description of this Stateful.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Stateful.
        The description for how the extension stores state

        :param description: The description of this Stateful.
        :type: str
        """

        self._description = description

    @property
    def scopes(self):
        """
        Gets the scopes of this Stateful.
        The scopes used to store state

        :return: The scopes of this Stateful.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this Stateful.
        The scopes used to store state

        :param scopes: The scopes of this Stateful.
        :type: list[str]
        """
        allowed_values = ["CLUSTER", "LOCAL"]
        if not set(scopes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `scopes` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(scopes)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._scopes = scopes

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
        if not isinstance(other, Stateful):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
