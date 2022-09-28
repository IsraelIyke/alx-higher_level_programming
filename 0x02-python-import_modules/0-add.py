#!/usr/bin/python
from add_0 import add

if __name__ == "__main__":
    import add_0

    add(int(add_0.argv[1]))

    a = 1
    b = 2
    func = add(a, b)
    print("{} + {} = {}".format(a, b, func))
