#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for j in my_list:
        count += 0
    if x > count:

        for i in range(x):
            if isinstance(my_list[i], int):
                try:
                    if i == x - 1:
                        print("{:d}".format(my_list[i]))
                    else:
                        print("{:d}".format(my_list[i]), end="")

                except Exception as e:
                    print("{}".format(e))
            else:
                continue
        return x
