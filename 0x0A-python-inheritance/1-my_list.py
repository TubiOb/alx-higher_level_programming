#!/usr/bin/python3
"""
This program creates a class called MyList that inherits from the class List
"""


class MyList(list):
    """
    This class inherits from the class list and can print its elements, sorted
    """

    def print_sorted(self):
        print(sorted(self))
