i#!/usr/bin/python3
"""
This program defines a LockedClass that you only can set
the attribute first_name
"""

class LockedClass():
    """
    This class is locked and you can only put the attribute first_name
    """

    __slots__ = ('first_name', )
