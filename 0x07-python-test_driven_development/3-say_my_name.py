#!/usr/bin/python3
"""
This program prints a message with the nexr=t format:
    My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints the naxt message: My name is <first name> <last name>
    Args:
      - first name: str
      - last name: str (Optional)
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
