#!/usr/bin/env python3
# def islower(c):
#     conv = ord(c)
#     for i in range(97, 123):
#         if conv == i:
#             return True
#         else:
#             return F
def islower(c):
    for i in range(97, 123):
        if ord(c) == i:
            return True
        else:
            return False
        # return i == ord(c)


islower("g")
