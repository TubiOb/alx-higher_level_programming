#!/usr/bin/python3
"""
This program uses the inherit for 'create Rectangle'
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle based in BaseGeometry
    """

    def __init__(self, width, height):
        """Constructor of Rectangle"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
