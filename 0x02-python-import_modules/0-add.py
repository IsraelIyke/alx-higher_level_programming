#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    add(int(sys.argv[1]))

a = 1
b = 2
func = add(a, b)
print("{} + {} = {}".format(a, b, func))
