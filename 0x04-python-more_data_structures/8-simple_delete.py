#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = a_dictionary.copy()
    if a_dictionary.get(key):
        del a[key]
        return a
    else:
        return a_dictionary
