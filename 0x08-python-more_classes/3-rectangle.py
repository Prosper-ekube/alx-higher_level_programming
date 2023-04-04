#!/usr/bin/python3
"""Defines a class of name Rectangle"""
class Rectangle:
    """Initializes the class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attruibute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be <= 0")
        else:
            self.__height = value

    def area(self):
        """"Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Returns printable string representation of the rectangle."""
        if self.__width != 0 and self.__height != 0:
            return "\n".join(f"{'#' * self.__width}"
                             for j in range(self.__height))
        else:
            return ""
