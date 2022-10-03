#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,)
    if len(tuple_b) < 2:
        tuple_b += (0,)

    if len(tuple_a) > 2 or len(tuple_b) > 2:
        for i in range(2):
            num_1 = tuple_a[i] + tuple_b[i]
            num_2 = tuple_a[i + 1] + tuple_b[i + 1]

    else:
        for i in range(len(tuple_a) - 1):
            num_1 = tuple_a[i] + tuple_b[i]
            num_2 = tuple_a[i + 1] + tuple_b[i + 1]

    return (num_1, num_2)
