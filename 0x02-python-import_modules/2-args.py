#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("{:d} argument:".format(len(argv)))
        for i in range(len(argv)):
            print("{:d}: {}".format(i, argv))
    elif len(argv) > 1:
        print("{:d} arguments:".format(len(argv)))
        for i in range(len(argv)):
            print("{:d}: {}".format(i, argv))
    else:
        print("{:d} arguments.".format(len(argv)))
