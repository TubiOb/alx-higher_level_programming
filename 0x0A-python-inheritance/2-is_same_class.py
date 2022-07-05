#!/usr/bin/python3
"""
This program validates if the object is the same with other class
"""


def is_same_class(obj, a_class):
    """
    This function validates if the obj is the same class of a_clas
    Args:
      - obj
      - a_class
    """
    return type(obj) == a_class
