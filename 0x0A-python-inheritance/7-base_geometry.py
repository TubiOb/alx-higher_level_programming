#!/usr/bin/python3
"""
This program has a class with a validator and an error
"""


class BaseGeometry():
    """
    This class contains an unimplemented method as well as a validator
    """

    def area(self):
        """
        This function raises an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates if the value is a integer.
        Args:
          - name: str
          - value: int
        """
        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
