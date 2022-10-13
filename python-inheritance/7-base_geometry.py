#!/usr/bin/python3
""" Module that contains a class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
