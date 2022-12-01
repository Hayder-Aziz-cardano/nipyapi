# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.19.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LabelDTO(object):
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
        'label': 'str',
        'width': 'float',
        'height': 'float',
        'getz_index': 'int',
        'style': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'versioned_component_id': 'versionedComponentId',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'label': 'label',
        'width': 'width',
        'height': 'height',
        'getz_index': 'getzIndex',
        'style': 'style'
    }

    def __init__(self, id=None, versioned_component_id=None, parent_group_id=None, position=None, label=None, width=None, height=None, getz_index=None, style=None):
        """
        LabelDTO - a model defined in Swagger
        """

        self._id = None
        self._versioned_component_id = None
        self._parent_group_id = None
        self._position = None
        self._label = None
        self._width = None
        self._height = None
        self._getz_index = None
        self._style = None

        if id is not None:
          self.id = id
        if versioned_component_id is not None:
          self.versioned_component_id = versioned_component_id
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if position is not None:
          self.position = position
        if label is not None:
          self.label = label
        if width is not None:
          self.width = width
        if height is not None:
          self.height = height
        if getz_index is not None:
          self.getz_index = getz_index
        if style is not None:
          self.style = style

    @property
    def id(self):
        """
        Gets the id of this LabelDTO.
        The id of the component.

        :return: The id of this LabelDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LabelDTO.
        The id of the component.

        :param id: The id of this LabelDTO.
        :type: str
        """

        self._id = id

    @property
    def versioned_component_id(self):
        """
        Gets the versioned_component_id of this LabelDTO.
        The ID of the corresponding component that is under version control

        :return: The versioned_component_id of this LabelDTO.
        :rtype: str
        """
        return self._versioned_component_id

    @versioned_component_id.setter
    def versioned_component_id(self, versioned_component_id):
        """
        Sets the versioned_component_id of this LabelDTO.
        The ID of the corresponding component that is under version control

        :param versioned_component_id: The versioned_component_id of this LabelDTO.
        :type: str
        """

        self._versioned_component_id = versioned_component_id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this LabelDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this LabelDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this LabelDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this LabelDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this LabelDTO.
        The position of this component in the UI if applicable.

        :return: The position of this LabelDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this LabelDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this LabelDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def label(self):
        """
        Gets the label of this LabelDTO.
        The text that appears in the label.

        :return: The label of this LabelDTO.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this LabelDTO.
        The text that appears in the label.

        :param label: The label of this LabelDTO.
        :type: str
        """

        self._label = label

    @property
    def width(self):
        """
        Gets the width of this LabelDTO.
        The width of the label in pixels when at a 1:1 scale.

        :return: The width of this LabelDTO.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this LabelDTO.
        The width of the label in pixels when at a 1:1 scale.

        :param width: The width of this LabelDTO.
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this LabelDTO.
        The height of the label in pixels when at a 1:1 scale.

        :return: The height of this LabelDTO.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this LabelDTO.
        The height of the label in pixels when at a 1:1 scale.

        :param height: The height of this LabelDTO.
        :type: float
        """

        self._height = height

    @property
    def getz_index(self):
        """
        Gets the getz_index of this LabelDTO.
        The z index of the label.

        :return: The getz_index of this LabelDTO.
        :rtype: int
        """
        return self._getz_index

    @getz_index.setter
    def getz_index(self, getz_index):
        """
        Sets the getz_index of this LabelDTO.
        The z index of the label.

        :param getz_index: The getz_index of this LabelDTO.
        :type: int
        """

        self._getz_index = getz_index

    @property
    def style(self):
        """
        Gets the style of this LabelDTO.
        The styles for this label (font-size : 12px, background-color : #eee, etc).

        :return: The style of this LabelDTO.
        :rtype: dict(str, str)
        """
        return self._style

    @style.setter
    def style(self, style):
        """
        Sets the style of this LabelDTO.
        The styles for this label (font-size : 12px, background-color : #eee, etc).

        :param style: The style of this LabelDTO.
        :type: dict(str, str)
        """

        self._style = style

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
        if not isinstance(other, LabelDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
