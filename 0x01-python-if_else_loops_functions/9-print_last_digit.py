#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        la = number / -1
        last = int(la % 10)
    else:
        last = number % 10
    print("{}".format(last), end="")
    return last
