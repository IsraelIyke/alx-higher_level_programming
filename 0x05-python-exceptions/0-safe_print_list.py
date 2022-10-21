#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for j in my_list:
        count += 1
    if x > count:
        for i in range(count):
            try:
                if i == x - 1:
                    print(my_list[i])
                    continue
                else:
                    print(my_list[i], end="")
            except Exception as e:
                print("there is an error here")
        return count
    else:
        for i in range(x):
            try:
                if i == x - 1:
                    print(my_list[i])
                    continue
                else:
                    print(my_list[i], end="")
            except Exception as e:
                print("there is an error here")
        return x
