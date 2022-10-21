#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lis = []
    for i in range(list_length):
        if isinstance((my_list_1[i] and my_list_2[i]), int):
            try:

                lis.append(my_list_1[i] / my_list_2[i])

            except ZeroDivisionError:
                print("{}".format("division by 0"))
            except IndexError:
                print("{}".format("out of range"))
            except ValueError:
                print("{}".format("out of range"))
        else:
            print("{}".format("wrong type"))
    return lis
