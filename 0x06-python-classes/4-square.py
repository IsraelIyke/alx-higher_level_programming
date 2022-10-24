#!/usr/bin/python3
"""A square module"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if int(size) < 0:
                raise ValueError("size must be >= 0")
            else:

                try:
                    self.__size = size

                except TypeError as e:
                    print(e)

    def size(self, value):
        return self.__size

    def area(self):
        return self.__size**2
