#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            if i == x - 1:
                print(my_list[i])
                continue
            else:
                print(my_list[i], end="")
        except Exception as e:
            print(e)
    return x
