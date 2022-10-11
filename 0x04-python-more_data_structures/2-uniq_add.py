#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    for i in range(len(my_list)):
        new_set.add(my_list[i])
    return sum(new_set)
