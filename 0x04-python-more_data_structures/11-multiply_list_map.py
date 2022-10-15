#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def multiply(number):
        return number * 2

    numbers = my_list.copy()
    result = map(multiply, numbers)
    return list(result)
