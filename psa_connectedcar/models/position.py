# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Position(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'type': 'str',
        'geometry': 'Point',
        'properties': 'PositionProperties'
    }

    attribute_map = {
        'type': 'type',
        'geometry': 'geometry',
        'properties': 'properties'
    }

    def __init__(self, type='Feature', geometry=None, properties=None):  # noqa: E501
        """Position - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._geometry = None
        self._properties = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if geometry is not None:
            self.geometry = geometry
        if properties is not None:
            self.properties = properties

    @property
    def type(self):
        """Gets the type of this Position.  # noqa: E501


        :return: The type of this Position.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Position.


        :param type: The type of this Position.  # noqa: E501
        :type: str
        """
        allowed_values = ["Feature"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def geometry(self):
        """Gets the geometry of this Position.  # noqa: E501


        :return: The geometry of this Position.  # noqa: E501
        :rtype: Point
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this Position.


        :param geometry: The geometry of this Position.  # noqa: E501
        :type: Point
        """

        self._geometry = geometry

    @property
    def properties(self):
        """Gets the properties of this Position.  # noqa: E501


        :return: The properties of this Position.  # noqa: E501
        :rtype: PositionProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Position.


        :param properties: The properties of this Position.  # noqa: E501
        :type: PositionProperties
        """

        self._properties = properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Position, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Position):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
