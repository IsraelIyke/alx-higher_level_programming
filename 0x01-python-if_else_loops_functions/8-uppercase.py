#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        # conv = ord(str[i])
        # conv = conv - 32
        # conv = chr(conv)
        # conv = uppercase(conv)
        str1 = ord(str[i])
        if str1 < 97:
            str2 = str1
        else:
            str2 = str1 - 32
        str3 = chr(str2)
        if i == len(str) - 1:
            print("{}".format(str3))
        else:
            print("{}".format(str3), end="")
