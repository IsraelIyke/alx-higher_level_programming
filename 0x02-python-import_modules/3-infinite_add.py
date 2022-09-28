#!/usr/bin/python3

from sys import argv


if __name__ == "__main__":
    count = 0
    for i in range(len(argv) - 1):

        count += int(argv[i + 1])
    print(count)
