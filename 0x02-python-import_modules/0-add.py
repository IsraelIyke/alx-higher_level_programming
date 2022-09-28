#!/usr/bin/python
from add_0 import add

a = 1
b = 2
func = add(a, b)

print("{} + {} = {}".format(a, b, func))

if __name__ == "__main__":
    import sys

    add(int(sys.argv[1]))
