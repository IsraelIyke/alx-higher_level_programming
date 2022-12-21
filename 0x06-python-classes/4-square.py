#!/usr/bin/python3
"""A square module"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        self.__size = size
        print(size**2)
        return size**2

    def size(self, value):
        self.my_var = value
        print(self.my_var**2)

    def area(self):
        return self.get_value()
